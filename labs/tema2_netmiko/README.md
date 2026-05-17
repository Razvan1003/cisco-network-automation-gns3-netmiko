# Tema 2 - GNS3 Network Automation with Netmiko

This lab automates a small GNS3 topology with Python and Netmiko. It configures VLAN segmentation, router-on-a-stick inter-VLAN routing, OSPF between routers and an ACL that blocks ICMP from VLAN 10 to VLAN 30 while permitting other traffic.

## Topology

```text
PC1 -- VLAN 10 -- ESW1 -- trunk -- R1 -- 10.0.13.0/30 -- R3 -- PC3 / VLAN 30
PC2 -- VLAN 20 -- ESW1
```

Main networks:

- VLAN 10: `192.168.10.0/24`, gateway `192.168.10.1`
- VLAN 20: `192.168.20.0/24`, gateway `192.168.20.1`
- VLAN 30: `192.168.30.0/24`, gateway `192.168.30.1`
- R1-R3 transit link: `10.0.13.0/30`

## What The Scripts Do

- `configure_sw1.py` creates VLAN 10 and VLAN 20, configures access ports and sets the uplink as trunk.
- `configure_r1.py` configures subinterfaces for VLAN 10/20, OSPF and the ICMP filtering ACL.
- `configure_r3.py` configures the R1-R3 link, VLAN 30 gateway and OSPF.
- `verify.py` runs show commands used to validate the lab.
- `run_all.py` applies the switch and router configuration in sequence.

## Files

```text
scripts/                  # Netmiko automation scripts
configs/                  # clean reference configs matching the scripts
topology/tema2_netmiko.gns3
validation/               # local output folder, ignored by Git except .gitkeep
```

## Requirements

- Python 3.10+
- GNS3
- Netmiko
- Cisco IOS nodes reachable through GNS3 Telnet console ports

Install dependencies from the repository root:

```bash
pip install -r requirements.txt
```

## Connection Settings

The scripts use Telnet console access exposed by GNS3.

Default lab values:

| Device | Host | Port |
| --- | --- | --- |
| R1 | `127.0.0.1` | `5001` |
| R3 | `127.0.0.1` | `5003` |
| SW1 / ESW1 | `192.168.233.128` | `5006` |

`SW1` uses port `5006` because the GNS3 topology exports `ESW1` on console port `5006`.

You can override defaults with environment variables:

```powershell
$env:R1_HOST="127.0.0.1"
$env:R1_PORT="5001"
$env:R3_HOST="127.0.0.1"
$env:R3_PORT="5003"
$env:SW1_HOST="192.168.233.128"
$env:SW1_PORT="5006"
```

If your nodes require login credentials, set:

```powershell
$env:LAB_USERNAME="admin"
$env:LAB_PASSWORD="password"
$env:LAB_SECRET="enable_password"
```

## Usage

From this folder:

```bash
python scripts/run_all.py
python scripts/verify.py
```

Run individual scripts when needed:

```bash
python scripts/configure_sw1.py
python scripts/configure_r1.py
python scripts/configure_r3.py
```

## Validation

Useful checks:

- `show vlan-switch`
- `show running-config`
- `show ip interface brief`
- `show ip protocols`
- `show ip ospf neighbor`
- `show access-lists`

Expected behavior:

- VLAN 10 and VLAN 20 are available on ESW1.
- R1 routes VLAN 10 and VLAN 20 through subinterfaces.
- R1 and R3 exchange routes with OSPF.
- ICMP echo from VLAN 10 to VLAN 30 is blocked by `BLOCK_VLAN10_ICMP`.
- Other IP traffic is permitted by the ACL.
