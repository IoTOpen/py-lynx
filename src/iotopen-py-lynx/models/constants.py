from typing import Final


class TraceObjectType:
    INSTALLATION: Final[str] = "installation"
    GATEWAY: Final[str] = "gateway"
    ORGANIZATION: Final[str] = "organization"
    USER: Final[str] = "user"
    DEVICE: Final[str] = "device"
    FUNCTION: Final[str] = "function"
    SCHEDULE: Final[str] = "schedule"
    NOTIFICATION_OUTPUT: Final[str] = "notification_output"
    NOTIFICATION_MESSAGE: Final[str] = "notification_message"
    OUTPUT_EXECUTOR: Final[str] = "output_executor"
    EDGE_APP: Final[str] = "edge_app"
    EDGE_APP_INSTANCE: Final[str] = "edge_app_instance"
    FILE: Final[str] = "file"
    ROLE: Final[str] = "role"
    GATEWAY_REGISTRATION_POLICY: Final[str] = "gateway_registration_policy"
    USER_REGISTRATION_POLICY: Final[str] = "user_registration_policy"
    MQTT: Final[str] = "mqtt"
    TRACE: Final[str] = "trace"


class TraceAction:
    CREATE: Final[str] = "create"
    DELETE: Final[str] = "delete"
    UPDATE: Final[str] = "update"
    VIEW: Final[str] = "view"
    FAILED: Final[str] = "failed"
    EXECUTE: Final[str] = "execute"
    AUTH: Final[str] = "auth"
