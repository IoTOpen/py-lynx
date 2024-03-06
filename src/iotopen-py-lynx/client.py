from typing import Optional

from src.lynx import *
from src.lynx.api_client import APIClient
from src.lynx.controller import *


class Client:

    def __init__(self, base_url: str, api_key: str):
        self.api_client = APIClient(base_url, api_key)
        self.__load_controllers()

    """
    Function
    """

    def get_functions(self, installation_id: int, filter: Optional[Filter] = None):
        return self._function_controller.get_functions(installation_id, filter)

    def get_function(self, installation_id: int, id: int):
        return self._function_controller.get_function(installation_id, id)

    def create_function(self, fun: Function):
        return self._function_controller.create_function(fun)

    def update_function(self, fun: Function):
        return self._function_controller.update_function(fun)

    def delete_function(self, fun: Function):
        return self._function_controller.delete_function(fun)

    def get_function_meta(self, installation_id: int, id: int, key: str):
        return self._function_controller.get_function_meta(installation_id, id, key)

    def create_function_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                             silent: Optional[bool] = False):
        return self._function_controller.create_function_meta(installation_id, id, key, meta, silent)

    def update_function_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                             silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        return self._function_controller.update_function_meta(installation_id, id, key, meta, silent, create_missing)

    def delete_function_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        return self._function_controller.delete_function_meta(installation_id, id, key, silent)

    """
    Device
    """

    def get_devices(self, installation_id: int, filter: Optional[Filter] = None):
        return self._device_controller.get_devices(installation_id, filter)

    def get_device(self, installation_id: int, id: int):
        return self._device_controller.get_device(installation_id, id)

    def create_device(self, dev: Device):
        return self._device_controller.create_device(dev)

    def update_device(self, dev: Device):
        return self._device_controller.update_device(dev)

    def delete_device(self, dev: Device):
        return self._device_controller.delete_device(dev)

    def get_device_meta(self, installation_id: int, id: int, key: str):
        return self._device_controller.get_device_meta(installation_id, id, key)

    def create_device_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                           silent: Optional[bool] = False):
        return self._device_controller.create_device_meta(installation_id, id, key, meta, silent)

    def update_device_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                           silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        return self._device_controller.update_device_meta(installation_id, id, key, meta, silent, create_missing)

    def delete_device_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        return self._device_controller.delete_device_meta(installation_id, id, key, silent)

    """
    Installation
    """

    def get_installations(self, filter: Optional[Filter] = None):
        return self._installation_controller.get_installations(filter)

    def get_installation(self, installation_id: int):
        return self._installation_controller.get_installation(installation_id)

    def create_installation(self, installation: Installation):
        return self._installation_controller.create_installation(installation)

    def update_installation(self, installation: Installation):
        return self._installation_controller.update_installation(installation)

    def delete_installation(self, installation: Installation):
        return self._installation_controller.delete_installation(installation)

    def get_installation_meta(self, installation_id: int, id: int, key: str):
        return self._installation_controller.get_installation_meta(installation_id, id, key)

    def create_installation_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                                 silent: Optional[bool] = False):
        return self._installation_controller.create_installation_meta(installation_id, id, key, meta, silent)

    def update_installation_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                                 silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        return self._installation_controller.update_installation_meta(installation_id, id, key, meta, silent,
                                                                      create_missing)

    def delete_installation_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        return self._installation_controller.delete_installation_meta(installation_id, id, key, silent)

    """
    Installation info
    """

    def get_installation_info(self, assigned_only: Optional[bool] = False):
        return self._installation_info_controller.get_installation_info(assigned_only)

    def get_installation_info_client_id(self, client_id: int, assigned_only: Optional[bool] = False):
        return self._installation_info_controller.get_installation_info_client_id(client_id, assigned_only)

    """
    User
    """

    def get_users(self, filter: Optional[Filter] = None):
        return self._user_controller.get_users(filter)

    def get_user(self, id: int):
        return self._user_controller.get_user(id)

    def create_user(self, user: User):
        return self._user_controller.create_user(user)

    def update_user(self, user: User):
        return self._user_controller.update_user(user)

    def delete_user(self, user: User):
        return self._user_controller.delete_user(user)

    def get_user_meta(self, id: int, key: str):
        return self._user_controller.get_user_meta(id, key)

    def create_user_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False):
        return self._user_controller.create_user_meta(id, key, meta, silent)

    def update_user_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False,
                         create_missing: Optional[bool] = False):
        return self._user_controller.update_user_meta(id, key, meta, silent, create_missing)

    def get_me(self):
        return self._user_controller.get_me()

    def update_me(self, user: User):
        return self._user_controller.update_me(user)

    """
    Schedule
    """

    def get_schedules(self, installation_id: int, executor: Optional[str] = None):
        return self._schedule_controller.get_schedules(installation_id, executor)

    def get_schedule(self, installation_id: int, id: int):
        return self._schedule_controller.get_schedule(installation_id, id)

    def create_schedule(self, schedule: Schedule):
        return self._schedule_controller.create_schedule(schedule)

    def update_schedule(self, schedule: Schedule):
        return self._schedule_controller.update_schedule(schedule)

    def delete_schedule(self, schedule: Schedule):
        return self._schedule_controller.delete_schedule(schedule)

    """
    Trace
    """

    def get_traces(self, fromm: Optional[float] = None, to: Optional[float] = None, limit: Optional[int] = 1000,
                   offset: Optional[int] = 0, order: Optional[str] = "desc",
                   object_type: Optional[str] = None, object_id: Optional[int] = None,
                   id: Optional[str] = None):
        return self._trace_controller.get_traces(fromm, to, limit, offset, order, object_type, object_id, id)

    """
    Organization
    """

    def get_organizations(self, minimal: Optional[bool] = False, filter: Optional[Filter] = None):
        return self._organization_controller.get_organizations(minimal, filter)

    def get_organization(self, id: int):
        return self._organization_controller.get_organization(id)

    def create_organization(self, org: Organization):
        return self._organization_controller.create_organization(org)

    def update_organization(self, org: Organization):
        return self._organization_controller.update_organization(org)

    def delete_organization(self, org: Organization, force: Optional[bool] = False):
        self._organization_controller.delete_organization(org, force)

    def force_password_reset(self, id: int):
        self._organization_controller.force_password_reset(id)

    def get_organization_meta(self, id: int, key: str):
        self._organization_controller.get_organization_meta(id, key)

    def create_organization_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False):
        self._organization_controller.create_organization_meta(id, key, meta, silent)

    def update_organization_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False,
                                 create_missing: Optional[bool] = False):
        self._organization_controller.update_organization_meta(id, key, meta, silent, create_missing)

    def delete_organization_meta(self, id: int, key: str, silent: Optional[bool] = False):
        self.delete_organization_meta(id, key, silent)

    """
    Notifications
    """

    def get_notification_messages(self, installation_id: int):
        return self._notification_controller.get_notification_messages(installation_id)

    def get_notification_message(self, installation_id: int, id: int):
        return self._notification_controller.get_notification_message(installation_id, id)

    def create_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        return self._notification_controller.create_notification_message(installation_id, notification_message)

    def update_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        return self._notification_controller.update_notification_message(installation_id, notification_message)

    def delete_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        return self._notification_controller.delete_notification_message(installation_id, notification_message)

    def get_notification_outputs(self, installation_id: int):
        return self._notification_controller.get_notification_outputs(installation_id)

    def get_notification_output(self, installation_id: int, id: int):
        return self._notification_controller.get_notification_output(installation_id, id)

    def create_notification_output(self, notification_output: NotificationOutput):
        return self._notification_controller.create_notification_output(notification_output)

    def update_notification_output(self, notification_output: NotificationOutput):
        return self._notification_controller.update_notification_output(notification_output)

    def delete_notification_output(self, notification_output: NotificationOutput):
        return self._notification_controller.delete_notification_output(notification_output)

    def get_notification_output_executors(self, installation_id: int):
        return self._notification_controller.get_notification_output_executors(installation_id)

    def get_notification_output_executor(self, installation_id: int, id: int):
        return self._notification_controller.get_notification_output_executor(installation_id, id)

    def send_notification(self, installation_id: int, output_id: int, data: Optional[dict[str, any]] = None):
        return self._notification_controller.send_notification(installation_id, output_id, data)

    """
    Log
    """

    def get_logs(self, installation_id: int, fromm: Optional[float] = None, to: Optional[float] = None,
                 limit: Optional[int] = 500, offset: Optional[int] = 0, order: Optional[str] = "desc",
                 topics: Optional[list[str]] = None):
        return self._log_controller.get_logs(installation_id, fromm, to, limit, offset, order, topics)

    def get_status(self, installation_id: int, topics: Optional[list[str]] = None):
        return self._log_controller.get_status(installation_id, topics)

    """
    Ege App
    """

    def get_edge_apps(self):
        return self._edge_app_controller.get_edge_apps()

    def get_edge_apps_organization(self, organization_id: int, available: Optional[bool] = False):
        return self._edge_app_controller.get_edge_apps_organization(organization_id, available)

    def get_edge_app(self, id: int):
        return self._edge_app_controller.get_edge_app(id)

    def create_edge_app(self, app: EdgeApp):
        return self._edge_app_controller.create_edge_app(app)

    def update_edge_app(self, app: EdgeApp):
        return self._edge_app_controller.update_edge_app(app)

    def delete_edge_app(self, app: EdgeApp):
        return self._edge_app_controller.delete_edge_app(app)

    def download_edge_app(self, id: int, version: str):
        return self._edge_app_controller.download_edge_app(id, version)

    def get_edge_app_versions(self, id: int, untagged: Optional[bool] = False):
        return self._edge_app_controller.get_edge_app_versions(id, untagged)

    def create_edge_app_version(self, id: int, lua: str, json: str):
        return self._edge_app_controller.create_edge_app_version(id, lua, json)

    def name_edge_app_version(self, id: int, version: EdgeAppVersion):
        return self._edge_app_controller.name_edge_app_version(id, version)

    def get_edge_app_config_options(self, id: int, version: str):
        return self._edge_app_controller.get_edge_app_config_options(id, version)

    def get_edge_app_instances(self, installation_id: int):
        return self._edge_app_controller.get_edge_app_instances(installation_id)

    def get_edge_app_instance(self, installation_id: int, instance_id: int):
        return self._edge_app_controller.get_edge_app_instance(installation_id, instance_id)

    def create_edge_app_instance(self, config: EdgeAppConfig):
        return self._edge_app_controller.create_edge_app_instance(config)

    def update_edge_app_instance(self, config: EdgeAppConfig):
        return self._edge_app_controller.update_edge_app_instance(config)

    def delete_edge_app_instance(self, config: EdgeAppConfig):
        return self._edge_app_controller.delete_edge_app_instance(config)

    """
    File
    """

    def get_files_installation(self, installation_id: int):
        return self._file_controller.get_files_installation(installation_id)

    def get_file_installation(self, installation_id: int, file_id: int):
        return self._file_controller.get_file_installation(installation_id, file_id)

    def get_files_organization(self, organization_id: int):
        return self._file_controller.get_files_organization(organization_id)

    def get_file_organization(self, organization_id: int, file_id: int):
        return self._file_controller.get_file_organization(organization_id, file_id)

    def create_file_installation(self, installation_id: int, file_name: str, mime: str, file):
        return self._file_controller.create_file_installation(installation_id, file_name, mime, file)

    def create_file_organization(self, organization_id: int, file_name: str, mime: str, file):
        return self._file_controller.create_file_organization(organization_id, file_name, mime, file)

    def update_file_installation(self, installation_id: int, file_name: str, mime: str, file):
        return self._file_controller.update_file_installation(installation_id, file_name, mime, file)

    def update_file_organization(self, organization_id: int, file_name: str, mime: str, file):
        return self._file_controller.update_file_organization(organization_id, file_name, mime, file)

    def delete_file_installation(self, installation_id: int, file_id: int):
        return self._file_controller.delete_file_installation(installation_id, file_id)

    def delete_file_organization(self, organization_id: int, file_id: int):
        return self._file_controller.delete_file_organization(organization_id, file_id)

    def download_file(self, hash: str):
        return self._file_controller.download_file(hash)

    """
    Internal
    """

    def __load_controllers(self):
        self._user_controller = UserController(self.api_client)
        self._function_controller = FunctionController(self.api_client)
        self._device_controller = DeviceController(self.api_client)
        self._installation_controller = InstallationController(self.api_client)
        self._installation_info_controller = InstallationInfoController(self.api_client)
        self._schedule_controller = ScheduleController(self.api_client)
        self._trace_controller = TraceController(self.api_client)
        self._organization_controller = OrganizationController(self.api_client)
        self._notification_controller = NotificationController(self.api_client)
        self._log_controller = LogController(self.api_client)
        self._edge_app_controller = EdgeAppController(self.api_client)
        self._file_controller = FileController(self.api_client)
