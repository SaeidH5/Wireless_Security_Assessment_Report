# Wireless Security - Report

## 📌 Project Overview
This repository contains the practical security assessment and simulation report. The project explores common wireless and local network vulnerabilities, focusing on Man-in-the-Middle (MITM) attacks, ARP/DNS spoofing, and effective defense-in-depth strategies.

📄 **[View Full Project Report (PDF)](PDF/wireless-security-report.pdf)**

---

## 🛠️ Lab Topology & Environment
The lab environment was simulated using a virtualized network setup consisting of:
* **Ubuntu Server (`10.10.0.10`):** Hosting an Apache HTTP/HTTPS server[cite: 4].
* **Windows 10 Client (`10.10.0.20`):** Target client machine[cite: 4].
* **Kali Linux Attacker (`10.10.0.30`):** Execution platform for network analysis and attack tools[cite: 4].

---

## 🔍 Key Attack Phases & Findings
1. **Traffic Analysis & Baseline:** Inspected cleartext HTTP payloads (`User-Agent`, `Host` headers) versus TLS-encrypted traffic structures.
2. **DNS Spoofing & Phishing:** Utilized `DNSChef` and custom login portals to redirect clients to rogue endpoints, highlighting browser certificate warning behaviors.
3. **ARP Spoofing & MITM:** Executed ARP cache poisoning alongside IP forwarding and `mitmproxy` to intercept credentials over a local area network.

---

## 🛡️ Mitigations & Defenses Evaluated
* **Transport Layer Security (HTTPS):** Encrypts web traffic payloads, protecting against passive sniffers.
* **VPN / SSH Tunneling:** Encapsulates network traffic, shielding client communications from local network-layer inspection.
* **Client Hardening:** Disabling auto-connect features to prevent malicious access point association.

---

## 📂 Repository Contents
* **`PDF`**: Contains the final formal technical report (`wireless-security-report.pdf`).
* **`captures`**: Wireshark `.pcap` files documenting baseline traffic, DNS spoofing, and MITM attacks.
* **`scripts`**: Python source code for security detection and server implementations.
* **`configs`**: SSL certificates, private keys, and operational log files.
* **`captive portal`**: HTML source files used for the captive portal simulation.
* **`video demo`**: Video walkthrough/demonstration of the lab execution (`Lab_Project Demo.mp4`).
