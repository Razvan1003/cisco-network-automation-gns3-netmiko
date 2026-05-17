from __future__ import annotations

import os
from typing import Any


def env_int(name: str, default: int) -> int:
    raw_value = os.environ.get(name)
    if raw_value is None or raw_value.strip() == "":
        return default
    return int(raw_value)


def lab_device(name: str, default_host: str, default_port: int) -> dict[str, Any]:
    username = os.environ.get("LAB_USERNAME", "")
    password = os.environ.get("LAB_PASSWORD", "")
    secret = os.environ.get("LAB_SECRET", "")
    return {
        "device_type": "cisco_ios_telnet",
        "host": os.environ.get(f"{name}_HOST", default_host),
        "port": env_int(f"{name}_PORT", default_port),
        "username": username,
        "password": password,
        "secret": secret,
        "fast_cli": False,
    }


DEVICES = {
    "SW1": lab_device("SW1", "192.168.233.128", 5006),
    "R1": lab_device("R1", "127.0.0.1", 5001),
    "R3": lab_device("R3", "127.0.0.1", 5003),
}
