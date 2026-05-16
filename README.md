# Cisco Network Automation - GNS3 and Netmiko

Python automation lab for Cisco-style network devices running in GNS3.

The project is designed as a public portfolio companion to the SmartOffice Packet Tracer project. It demonstrates how network configuration can be backed up, verified and updated with Python and Netmiko.

## Goals

- Connect to lab routers/switches with Netmiko
- Back up running configurations
- Run standard verification commands
- Push small configuration snippets safely
- Keep credentials out of source control
- Document repeatable GNS3 network automation workflows

## Repository Structure

```text
inventory.example.yml      # example device inventory
requirements.txt           # Python dependencies
scripts/
  backup_configs.py        # saves running-config output
  verify_connectivity.py   # runs show commands and stores outputs
  push_config.py           # pushes a selected config snippet
configs/
  sample_banner.cfg        # safe example config snippet
validation/
  .gitkeep                 # output folder for verification logs
docs/
  lab-topology.md          # topology notes
```

## Requirements

- Python 3.10+
- GNS3 lab with SSH reachable network devices
- Netmiko-supported Cisco IOS devices

Install dependencies:

```bash
pip install -r requirements.txt
```

## Inventory

Copy `inventory.example.yml` to `inventory.yml` and adjust hostnames/IP addresses for your GNS3 lab.

Credentials should be supplied through environment variables, not committed to GitHub.

Example:

```powershell
$env:LAB_USERNAME="admin"
$env:LAB_PASSWORD="your_password"
```

## Usage

Back up running configurations:

```bash
python scripts/backup_configs.py --inventory inventory.yml --output backups
```

Run verification commands:

```bash
python scripts/verify_connectivity.py --inventory inventory.yml --output validation
```

Push a config snippet to one device:

```bash
python scripts/push_config.py --inventory inventory.yml --device R1 --config configs/sample_banner.cfg
```

## Security Notes

- Do not commit real passwords, tokens or private IP plans from non-lab environments.
- Use this only in a lab or with explicit permission.
- Start with read-only backup and verification scripts before pushing configuration.

## Roadmap

- Add GNS3 topology screenshot
- Add sample validation outputs
- Add VLAN and routing automation examples
- Add pre-change and post-change verification
