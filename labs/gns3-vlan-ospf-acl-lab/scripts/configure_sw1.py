from __future__ import annotations

from netmiko import ConnectHandler

from devices import DEVICES


SW1_CONFIG = [
    "interface fastEthernet1/0",
    "switchport mode access",
    "switchport access vlan 10",
    "no shutdown",
    "exit",
    "interface fastEthernet1/1",
    "switchport mode access",
    "switchport access vlan 20",
    "no shutdown",
    "exit",
    "interface fastEthernet1/2",
    "switchport mode trunk",
    "no shutdown",
    "exit",
    "no ip domain-lookup",
]


def create_vlans(conn) -> str:
    output = ""
    output += conn.send_command_timing("vlan database")
    output += conn.send_command_timing("vlan 10")
    output += conn.send_command_timing("vlan 20")
    output += conn.send_command_timing("exit")
    return output


def main() -> None:
    conn = ConnectHandler(**DEVICES["SW1"])
    try:
        output = create_vlans(conn)
        output += conn.send_config_set(SW1_CONFIG)
        output += conn.save_config()
        print(output)
    finally:
        conn.disconnect()


if __name__ == "__main__":
    main()
