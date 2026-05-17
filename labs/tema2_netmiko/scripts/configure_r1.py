from __future__ import annotations

from netmiko import ConnectHandler

from devices import DEVICES


R1_CONFIG = [
    "no router ospf 1",
    "interface fastEthernet0/0",
    "no ip address",
    "no shutdown",
    "exit",
    "interface fastEthernet0/0.10",
    "encapsulation dot1Q 10",
    "ip address 192.168.10.1 255.255.255.0",
    "exit",
    "interface fastEthernet0/0.20",
    "encapsulation dot1Q 20",
    "ip address 192.168.20.1 255.255.255.0",
    "exit",
    "interface fastEthernet0/1",
    "ip address 10.0.13.1 255.255.255.252",
    "no shutdown",
    "exit",
    "router ospf 1",
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    "network 10.0.13.0 0.0.0.3 area 0",
    "exit",
    "ip access-list extended BLOCK_VLAN10_ICMP",
    "deny icmp 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255 echo",
    "permit ip any any",
    "exit",
    "interface fastEthernet0/0.10",
    "ip access-group BLOCK_VLAN10_ICMP in",
    "exit",
]


def main() -> None:
    conn = ConnectHandler(**DEVICES["R1"])
    try:
        output = conn.send_config_set(R1_CONFIG)
        output += conn.save_config()
        print(output)
    finally:
        conn.disconnect()


if __name__ == "__main__":
    main()
