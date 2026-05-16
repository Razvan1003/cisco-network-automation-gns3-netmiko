from __future__ import annotations

import argparse
from pathlib import Path

from netmiko import ConnectHandler

from common import connection_params, load_inventory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Push a config snippet to one lab device.")
    parser.add_argument("--inventory", default="inventory.yml")
    parser.add_argument("--device", required=True, help="Device name from inventory.yml")
    parser.add_argument("--config", required=True, help="Path to config snippet")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    devices = {device["name"]: device for device in load_inventory(args.inventory)}
    if args.device not in devices:
        raise SystemExit(f"Device not found in inventory: {args.device}")

    commands = [
        line.strip()
        for line in Path(args.config).read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("!")
    ]
    if not commands:
        raise SystemExit("Config snippet is empty")

    device = devices[args.device]
    print(f"Pushing {len(commands)} command(s) to {device['name']} ({device['host']})")
    with ConnectHandler(**connection_params(device)) as connection:
        connection.enable()
        output = connection.send_config_set(commands)
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
