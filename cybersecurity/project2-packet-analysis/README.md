# Network Traffic Capture Analysis

A packet capture analysis project using Wireshark, completed as a final project for a Cybersecurity Essentials: Networking course.

## Assignment

Analyze a provided `.pcap` packet capture file, answer a set of predefined objectives about the network traffic, identify security issues and anomalies, and provide actionable security recommendations.

## What was analyzed

The `http.cap` file contains a captured HTTP session in which a client accesses a web page and downloads additional advertising content from a secondary server.

### Key participants

| Role | IP Address |
|------|------------|
| Client | 145.254.160.237 |
| Web server | 65.208.228.223 |
| Google ad server | 216.239.59.99 |

### What was found

- Two distinct TCP streams identified
- Standard three-way handshake observed (SYN → SYN/ACK → ACK)
- HTTP GET request to `/download.html` (packet 4), server responded with HTTP 200 OK (packet 27)
- Secondary HTTP GET request to Google advertising service detected (packet 18)
- All HTTP traffic transmitted unencrypted — a security vulnerability
- DNS requests analyzed to trace domain resolution
- Performance issues and security recommendations documented in the full report

## Technologies

- [Wireshark](https://www.wireshark.org) v4.4.9 — packet capture analysis
- HTTP, TCP, DNS protocol analysis
- TCP stream following and filtering

## Project files

| File | Description |
|------|-------------|
| `http.cap` | Packet capture file (open in Wireshark) |
| `Network Traffic Capture Analytics Report.odt` | Full analysis report with findings and security recommendations |
| `HTTP Objectives_Answers.docx` | Answers to the predefined project objectives |

## How to open

1. Install [Wireshark](https://www.wireshark.org/download.html)
2. Open `http.cap` directly in Wireshark
3. Use display filters (e.g. `http`, `tcp`, `dns`) to explore the traffic

## Notes

This is a final project completed as part of a Cybersecurity Essentials: Networking course at CanCode Communities, New York.