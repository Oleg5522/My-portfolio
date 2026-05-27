# VLAN Network Design

A network topology project designed and implemented in Cisco Packet Tracer as part of a Cybersecurity Essentials: Networking course.

## Assignment

Design and implement an original network with logical segmentation using VLANs. Minimum requirements: 8 end devices, 3 switches, 4 VLANs. Creativity and additional features improving scalability or security were encouraged.

## What was built

The network exceeds the minimum requirements — it includes one router, four switches, and nine end devices grouped by functional roles across four VLANs.

### Network topology

A hierarchical topology where Switch3 acts as the central distribution switch. Switch0, Switch1, and Switch2 are access layer switches serving their device groups. Router0 handles inter-VLAN routing using Router-on-a-Stick technology and serves as a gateway for ACL security policies.

### VLANs configured

| VLAN ID | Name | Subnet | Devices |
|---------|------|--------|---------|
| 10 | Director | 192.168.10.0/24 | Director PC |
| 20 | IT | 192.168.20.0/24 | SysAdmin PC, Server |
| 30 | Administration | 192.168.30.0/24 | Accountant Laptop, Lawyer Laptop |
| 40 | General | 192.168.40.0/24 | Remaining end devices |

## Technologies

- Cisco Packet Tracer — network simulation
- VLANs — logical network segmentation
- Router-on-a-Stick — inter-VLAN routing
- ACL (Access Control Lists) — traffic filtering and security policies
- Trunk links — inter-switch VLAN traffic

## Project files

| File | Description |
|------|-------------|
| `Project1_.pkt` | Cisco Packet Tracer network topology file |
| `Project1_.odt` | Full project report with configuration details and test results |
| `Create a network top.png` | Network topology diagram |
| `analyze the uploaded.png` | Connectivity test results |
| `Equipment.ods` | Equipment list |
| `Vlan.ods` | VLAN configuration table |

## How to open

Open `Project1_.pkt` in [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer). Free registration required.

## Notes

This is a midterm project completed as part of a Cybersecurity Essentials: Networking course at CanCode Communities, New York.