# GNS3 Lab Topology

The repository includes a complete Netmiko lab under `labs/tema2_netmiko/`.

## Tema 2 Topology

```text
PC1 -- VLAN 10 -- ESW1 -- trunk -- R1 -- 10.0.13.0/30 -- R3 -- PC3 / VLAN 30
PC2 -- VLAN 20 -- ESW1
```

## Devices

| Device | Role |
| --- | --- |
| `ESW1` | VLAN access switch and trunk uplink |
| `R1` | router-on-a-stick for VLAN 10/20 and OSPF peer |
| `R3` | VLAN 30 gateway and OSPF peer |
| `PC1` | VLAN 10 host |
| `PC2` | VLAN 20 host |
| `PC3` | VLAN 30 host |

## Addressing

| Segment | Network | Gateway / Interface |
| --- | --- | --- |
| VLAN 10 | `192.168.10.0/24` | `192.168.10.1` |
| VLAN 20 | `192.168.20.0/24` | `192.168.20.1` |
| VLAN 30 | `192.168.30.0/24` | `192.168.30.1` |
| R1-R3 link | `10.0.13.0/30` | `10.0.13.1`, `10.0.13.2` |

## Automation Scope

- Create VLANs on `ESW1`
- Configure access ports and trunk uplink
- Configure R1 subinterfaces for inter-VLAN routing
- Configure OSPF on `R1` and `R3`
- Apply an ACL that blocks ICMP echo from VLAN 10 to VLAN 30
- Run verification commands with Netmiko
