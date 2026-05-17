from __future__ import annotations

from netmiko import ConnectHandler

from devices import DEVICES


R3_CONFIG = [
    "no router ospf 1",
    "interface fastEthernet0/0",
    "ip address 10.0.13.2 255.255.255.252",
    "no shutdown",
    "exit",
    "interface fastEthernet0/1",
    "ip address 192.168.30.1 255.255.255.0",
    "no shutdown",
    "exit",
    "router ospf 1",
    "network 10.0.13.0 0.0.0.3 area 0",
    "network 192.168.30.0 0.0.0.255 area 0",
    "exit",
]


def main() -> None:
    conn = ConnectHandler(**DEVICES["R3"])
    try:
        output = conn.send_config_set(R3_CONFIG)
        output += conn.save_config()
        print(output)
    finally:
        conn.disconnect()


if __name__ == "__main__":
    main()
