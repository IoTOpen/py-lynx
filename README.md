# Python Lynx

This is a wrapper library for the [IoT Open Lynx platform API:s][0]. Most API-calls
are exposed as a `Client` class with functions for every API-endpoint. All
models are also implemented as classes.

## Install

Run the following command to install the package using pip:
```bash
python3 -m pip install --upgrade iotopen-py-lynx
```

## Usage

Create a Lynx client and use the functions on it to make API-calls.

```python
from iotopen-py-lynx import Client

cli = Client("https://lynx.iotopen.se", "abcdef123456789abcdef123456789")

installations = cli.get_installations()
print(installations)
```

[0]: https://iotopen.io/developers