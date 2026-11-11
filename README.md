# RackMind - AI DCIM Copilot for Homelab & Edge Data Centers

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

> The $10k DCIM Alternative. An AI agent that watches your rack 24/7, predicts failures, and cuts your PUE.

Traditional DCIM like Schneider StruxureWareWare or Sunbird costs $10,000+/year. RackMind gives you 80% of the power for your homelab with open source stack.

### 🎥 Demo
- Grafana Dashboard with real-time PUE, Temperature, Power
- Slack/Discord bot: Ask "is rack 2 hot? summarize last night"

![Cover](https://raw.githubusercontent.com/seelzaza/rackmind/main/docs/cover.png)

### ✨ Features

**1. 24/7 Facility Monitoring**
- SNMP for APC UPS, Eaton, Raritan PDU
- Redfish for Dell iDRAC, HPE iLO
- IPMI for Supermicro
- Proxmox / Unraid API

**2. PUE & Cost Saver Brain**
```
PUE = Total Facility Power / IT Equipment Power
Wasted Cost = (Total - IT) * $0.15 * hours
```
Example: "Your PUE was 1.82 yesterday. You wasted $14.20. Tip: Increase setpoint from 72°F to 77°F to save ~$280/month"

**3. Predictive Failure Engine**
Uses IsolationForest to detect:
- AC cooling efficiency degradation
- Fan RPM drop (predict failure 11 days early)
- UPS battery runtime degraded

**4. Chat with Your Rack**
Slack / Discord / Telegram bot powered by GPT-4o.

### 🚀 Quick Start (10 mins)

```bash
git clone https://github.com/yourname/rackmind.git
cd rackmind
cp .env.example .env
# Edit .env - add OPENAI_API_KEY, SLACK_BOT_TOKEN
docker-compose up -d
# Open Grafana: http://localhost:3000 (admin/admin)
# Invite Slack bot to your channel: /invite @rackmind
```

### 📁 Project Structure

```
rackmind/
├── docker-compose.yml
├── collector/collector.py  # SNMP + Redfish collector
├── brain/
│   ├── prompts_en.py       # AI prompts for PUE, RCA
│   ├── predictive.py       # Anomaly detection (Pro)
│   └── cost_report.py      # PDF report (Pro)
├── bot/
│   ├── slack_bot.py
│   └── discord_bot.py
├── grafana/dashboard.json
└── docs/
```

### 🔧 Connect Real Hardware

**APC UPS via SNMP:**
```python
# Edit collector/collector.py
from pysnmp.hlapi import *
# OID for APC UPS load: .1.3.6.1.4.1.318.1.1.1.12.2.3.1.1.2.1
```

**Dell iDRAC via Redfish:**
```python
import redfish
client = redfish.redfish_client(base_url="https://192.168.1.100", username="root", password="calvin")
client.login()
thermal = client.get("/redfish/v1/Chassis/System.Embedded.1/Thermal")
```

**Proxmox:**
```python
from proxmoxer import ProxmoxAPI
proxmox = ProxmoxAPI('192.168.1.100', user='root@pam', password='secret', verify_ssl=False)
```

### 🧠 AI Prompts

See `brain/prompts_en.py` - Includes:
- PUE_ANALYSIS_PROMPT
- RCA_PROMPT (Root Cause Analysis)
- CHAT_PROMPT

### 📊 Grafana Dashboard

Import `grafana/dashboard.json` into Grafana. Includes:
- PUE Real-time
- Temperature per rack
- Power IT vs Total
- Wasted Cost Today

### 💡 Why I Built This

I run a small 2-rack setup at home and couldn't justify $10k/yr for proper DCIM. So I built RackMind to:
- Stop waking up at 3 AM because AC failed
- Calculate real PUE and save on power bill
- Predict failures before they happen

### 🤝 Contributing

PRs welcome! Especially for:
- More hardware collectors (Eaton, Vertiv, etc.)
- Better anomaly detection models
- Discord/Telegram improvements

### 📦 Pro Version

The open source version includes everything you need for 1-2 racks.

For those who want to support and get:
- Up to 5 racks
- Commercial use license
- Auto PDF cost reports
- Predictive module pre-trained

Available on Gumroad (optional): https://seelzaza.gumroad.com/l/gurrka

### 📄 License

MIT License - See LICENSE file.

### 🙏 Acknowledgments

- r/homelab community for feedback
- Grafana, InfluxDB, Slack Bolt

---
**Looking for feedback:** Using IsolationForest for fan failure prediction - anyone done similar with homelab data?
