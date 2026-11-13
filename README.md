# Python Lynx

A Python wrapper library for the [IoT Open Lynx platform API][0]. All API-calls
are exposed as methods on a single `Client` class, and the objects returned by
the API (installations, devices, functions, schedules and so on) are
implemented as model classes.

## Install

Requires Python 3.9 or later. Install the package using pip:

```bash
python3 -m pip install --upgrade iotopen-py-lynx
```

The package is installed as `iotopen-py-lynx` but imported as `lynx`.

## Getting started

You need two things to create a client:

1. The URL of your Lynx server, for example `https://lynx.iotopen.se`.
2. An API key, created on your user in Lynx.

Avoid writing the API key in your code. Read it from an environment variable
instead:

```bash
export LYNX_URL="https://lynx.iotopen.se"
export LYNX_API_KEY="your-api-key"
```

```python
import os

from lynx import Client

cli = Client(os.environ["LYNX_URL"], os.environ["LYNX_API_KEY"])

for installation in cli.get_installations():
    print(installation.id, installation.name)
```

The rest of the examples assume that `cli` has been created like above.

## Concepts

Lynx organizes data in a few kinds of objects:

- **Installation**: a site, such as a home or a building. It owns devices and
  functions. Most calls take an `installation_id`.
- **Device**: a piece of hardware, such as a sensor or a wall plug.
- **Function**: one thing you can read or control, such as a temperature or an
  on/off switch. A function usually belongs to a device through the
  `device_id` metadata.
- **Metadata**: free-form key/value strings on every object, for example
  `name`, `unit`, `topic_read` and `topic_write`.

Values are sent and received over MQTT. A function reports its value on the
topic in its `topic_read` metadata and is controlled through the topic in its
`topic_write` metadata.

## Examples

### Installations

```python
installations = cli.get_installations()

installation = cli.get_installation(1234)
print(installation.name, installation.client_id)
```

### Functions and devices

```python
from lynx import Filter

functions = cli.get_functions(1234)

for fn in functions:
    print(fn.id, fn.type, fn.meta.get("name"), fn.meta.get("topic_read"))

# Filter on type and/or metadata. Wildcards are supported in values.
temperatures = cli.get_functions(1234, Filter({"type": "temperature"}))
kitchen = cli.get_functions(1234, Filter({"name": "Kitchen*"}))

function = cli.get_function(1234, 42)
devices = cli.get_devices(1234)
device = cli.get_device(1234, 7)
```

### Search

`search` finds installations, devices and functions by name, description,
metadata or ID across everything you have access to. Use `*` as a wildcard.

```python
result = cli.search("kitchen*", types=["function"], metadata={"unit": "°C"})

print(result.total, "matches")
for entry in result.results:
    print(entry.type, entry.id, entry.name, entry.installation_id)
```

Results are paginated with `limit` and `offset`. The search endpoint is in beta
in the Lynx API.

### Read current values

`get_status` returns the latest known value for every topic in an installation.
Pass a list of topics to only get some of them.

```python
for entry in cli.get_status(1234):
    print(entry.topic, entry.value, entry.timestamp)
```

### Read historical values

`get_logs` returns a page of log entries. By default it returns the last 24
hours, newest first. Timestamps are Unix timestamps in seconds.

```python
import time

page = cli.get_logs(
    1234,
    fromm=time.time() - 7 * 24 * 3600,  # one week back
    to=time.time(),
    limit=100,
    topics=["obj/zwave/temperature/5"],
)

print(page.total, "entries in total")
for entry in page.data:
    print(entry.timestamp, entry.value)
```

Use `offset` to fetch the next page.

### Control a function

Look up the function's `topic_write` metadata and publish a value to it:

```python
function = cli.get_function(1234, 42)

cli.mqtt_publish(1234, function.meta["topic_write"], {"value": 1})
```

`mqtt_publish` accepts any JSON-serializable payload.

### Create, update and delete

Create objects from the model classes. Update and delete take the object
itself.

```python
from lynx import Device, Function, Meta

device = cli.create_device(Device(
    installation_id=1234,
    type="sensor",
    meta=Meta({"name": "Living room sensor"}),
))

function = cli.create_function(Function(
    installation_id=1234,
    type="temperature",
    meta=Meta({
        "name": "Living room temperature",
        "device_id": str(device.id),
        "topic_read": "obj/custom/livingroom/temperature",
        "unit": "°C",
    }),
))

function.meta["name"] = "Living room temp"
cli.update_function(function)

cli.delete_function(function)
cli.delete_device(device)
```

### Metadata

Single metadata keys can also be read and written directly. All values are
strings.

```python
from lynx import MetaObject

cli.create_function_meta(1234, 42, "location", MetaObject("Kitchen"))
cli.update_function_meta(1234, 42, "location", MetaObject("Hallway"))
print(cli.get_function_meta(1234, 42, "location").value)
cli.delete_function_meta(1234, 42, "location")

cli.update_installation_meta(1234, "owner", MetaObject("Jane"), create_missing=True)
```

The same methods exist for devices, users and organizations.

### Schedules

```python
from lynx import Schedule

schedule = cli.create_schedule(Schedule(
    installation_id=1234,
    executor="cloud",
    active=True,
    day_of_week="1-5",  # Monday to Friday
    day_of_month="*",
    month="*",
    hour="7",
    minute="0",
    topic="obj/zwave/switch/5/set",
    value=1,
))

for s in cli.get_schedules(1234):
    print(s.id, s.hour, s.minute, s.topic, s.value)
```

### Notifications

```python
outputs = cli.get_notification_outputs(1234)

cli.send_notification(1234, outputs[0].id, {"message": "Hello from Python"})
```

### Files

Files can be stored on an installation or an organization. `file` can be bytes
or an open file.

```python
with open("floorplan.png", "rb") as f:
    file = cli.create_file_installation(1234, "floorplan.png", "image/png", f)

print(file.id, file.hash)

for f in cli.get_files_installation(1234):
    print(f.id, f.name, f.mime)

data = cli.download_file(file.hash)  # bytes

cli.update_file_installation(1234, file.id, "floorplan.png", "image/png", data)
cli.delete_file_installation(1234, file.id)
```

The same methods exist for organizations, for example `create_file_organization`.

### Roles and permissions

`get_permissions` returns what the authenticated user is allowed to do, as a
map from permission to `True`/`False`. Permissions follow the MQTT topic
pattern, where `+` and `#` are wildcards. Permissions that are not listed are
not allowed.

```python
permissions = cli.get_permissions()
print(permissions.get("device/#", False))
```

Roles group permissions together:

```python
from lynx import Role

for role in cli.get_roles():
    print(role.id, role.name, role.priority)

role = cli.create_role(Role(
    name="Viewer",
    permissions={"functionx/+/add": True},
    priority=10,
))

role.name = "Read only"
cli.update_role(role)

cli.delete_role(role)
```

### Error handling

API errors raise `HTTPException`, which carries the HTTP status code and the
message from the server:

```python
from lynx import HTTPException

try:
    cli.get_installation(1234)
except HTTPException as e:
    print(e.status_code, e.message)
```

## Available methods

| Area              | Methods                                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Installations     | `get_installations`, `get_installation`, `create_installation`, `update_installation`, `delete_installation`, `*_installation_meta` |
| Installation info | `get_installation_info`, `get_installation_info_client_id`                                                                         |
| Devices           | `get_devices`, `get_device`, `create_device`, `update_device`, `delete_device`, `*_device_meta`                                     |
| Functions         | `get_functions`, `get_function`, `create_function`, `update_function`, `delete_function`, `*_function_meta`                         |
| Values            | `get_status`, `get_logs`, `mqtt_publish`                                                                                           |
| Schedules         | `get_schedules`, `get_schedule`, `create_schedule`, `update_schedule`, `delete_schedule`                                           |
| Users             | `get_me`, `update_me`, `get_users`, `get_user`, `create_user`, `update_user`, `delete_user`, `*_user_meta`                         |
| Organizations     | `get_organizations`, `get_organization`, `create_organization`, `update_organization`, `delete_organization`, `force_password_reset`, `*_organization_meta` |
| Notifications     | `get_notification_messages`, `get_notification_outputs`, `get_notification_output_executors`, `send_notification` and CRUD        |
| Edge apps         | `get_edge_apps`, `get_edge_app`, `get_edge_app_publisher`, `get_edge_app_versions`, `get_edge_app_instances` and CRUD                                |
| Search            | `search`                                                                                                                           |
| Files             | `get_files_*`, `get_file_*`, `create_file_*`, `update_file_*`, `delete_file_*` (installation and organization), `download_file`  |
| Roles             | `get_roles`, `get_role`, `create_role`, `update_role`, `delete_role`, `get_permissions`                                            |
| Trace             | `get_traces`                                                                                                                       |

`*_meta` means `get_`, `create_`, `update_` and `delete_` variants.

See the [API documentation][1] for details about each endpoint.

## License

Apache License 2.0, see [LICENSE](LICENSE).

[0]: https://iotopen.io/developers
[1]: https://lynx.iotopen.se/api-doc/
