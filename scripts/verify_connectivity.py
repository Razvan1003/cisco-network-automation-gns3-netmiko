from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from netmiko import ConnectHandler

from common import connection_params, load_inventory


VERIFY_COMMANDS = [
    "show ip interface brief",
    "show ip route",
    "show vlan brief",
    "show interfaces trunk",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run standard verification commands.")
    parser.add_argument("--inventory", default="inventory.yml")
    parser.add_argument("--output", default="validation")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for device in load_inventory(args.inventory):
        print(f"Verifying {device['name']} ({device['host']})")
        sections: list[str] = []
        with ConnectHandler(**connection_params(device)) as connection:
            connection.enable()
            for command in VERIFY_COMMANDS:
                output = connection.send_command(command)
                sections.append(f"## {command}\n\n{output}\n")

        output_path = output_dir / f"{device['name']}_verification_{timestamp}.txt"
        output_path.write_text("\n".join(sections), encoding="utf-8")
        print(f"Saved {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
