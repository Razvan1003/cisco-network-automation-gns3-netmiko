from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


def load_inventory(path: str | Path) -> list[dict[str, Any]]:
    inventory_path = Path(path)
    with inventory_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    devices = data.get("devices", [])
    if not isinstance(devices, list):
        raise ValueError("inventory file must contain a 'devices' list")
    return [build_device(device) for device in devices]


def build_device(device: dict[str, Any]) -> dict[str, Any]:
    username = value_from_env(device, "username", "username_env")
    password = value_from_env(device, "password", "password_env")
    return {
        "name": device["name"],
        "host": device["host"],
        "device_type": device.get("device_type", "cisco_ios"),
        "username": username,
        "password": password,
    }


def value_from_env(device: dict[str, Any], value_key: str, env_key: str) -> str:
    if value_key in device:
        return str(device[value_key])
    env_name = device.get(env_key)
    if not env_name:
        raise ValueError(f"{device.get('name', 'device')} is missing {value_key} or {env_key}")
    value = os.environ.get(str(env_name))
    if not value:
        raise ValueError(f"environment variable {env_name} is not set")
    return value


def connection_params(device: dict[str, Any]) -> dict[str, Any]:
    return {
        "device_type": device["device_type"],
        "host": device["host"],
        "username": device["username"],
        "password": device["password"],
    }
