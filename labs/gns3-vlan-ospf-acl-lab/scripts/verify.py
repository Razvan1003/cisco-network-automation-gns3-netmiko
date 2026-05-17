from __future__ import annotations

from netmiko import ConnectHandler

from devices import DEVICES


SHOW_COMMANDS = {
    "SW1": [
        "show vlan-switch",
        "show running-config",
    ],
    "R1": [
        "show ip interface brief",
        "show ip protocols",
        "show ip ospf neighbor",
        "show access-lists",
    ],
    "R3": [
        "show ip interface brief",
        "show ip protocols",
        "show ip ospf neighbor",
    ],
}


def main() -> None:
    for name, device in DEVICES.items():
        print(f"\n{'-' * 20} {name} {'-' * 20}")
        conn = ConnectHandler(**device)
        try:
            for command in SHOW_COMMANDS[name]:
                print(f"\n--- {command} ---")
                print(conn.send_command(command))
        finally:
            conn.disconnect()


if __name__ == "__main__":
    main()
