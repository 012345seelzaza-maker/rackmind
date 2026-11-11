
import time, random
from datetime import datetime

# Simple collector simulation - replace with real SNMP/Redfish calls
# For APC UPS: use pysnmp, for Dell iDRAC: use redfish library

def collect_metrics():
    # In production: snmp_get for UPS, redfish for iDRAC
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "rack_id": "RACK-01",
        "temperature_c": round(24 + random.uniform(-1, 4), 2),
        "humidity": round(45 + random.uniform(-5, 15), 2),
        "it_power_kw": round(3.2 + random.uniform(-0.3, 0.5), 2),
        "total_power_kw": round(5.5 + random.uniform(-0.5, 0.8), 2),
        "pue": 0,
        "fan_rpm": int(4500 + random.uniform(-500, 500)),
    }

def calculate_pue(total, it):
    return round(total / it, 2) if it > 0 else 0

if __name__ == "__main__":
    while True:
        m = collect_metrics()
        m["pue"] = calculate_pue(m["total_power_kw"], m["it_power_kw"])
        print(f"[{m['timestamp']}] PUE: {m['pue']} | Temp: {m['temperature_c']}C | IT Power: {m['it_power_kw']}kW")
        # TODO: write to InfluxDB
        time.sleep(30)
