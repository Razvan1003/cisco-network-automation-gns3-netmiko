from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from netmiko import ConnectHandler

from common import connection_params, load_inventory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Back up running configs from lab devices.")
    parser.add_argument("--inventory", default="inventory.yml")
    parser.add_argument("--output", default="backups")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for device in load_inventory(args.inventory):
        print(f"Connecting to {device['name']} ({device['host']})")
        with ConnectHandler(**connection_params(device)) as connection:
            connection.enable()
            config = connection.send_command("show running-config")
        output_path = output_dir / f"{device['name']}_running_config_{timestamp}.txt"
        output_path.write_text(config + "\n", encoding="utf-8")
        print(f"Saved {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
