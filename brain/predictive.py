
from sklearn.ensemble import IsolationForest
import numpy as np

# Simple anomaly detector for Pro Edition
# Train on 7 days of normal data, predict failures

class PredictiveEngine:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)
        self.baseline = None

    def train(self, historical_metrics):
        # historical_metrics: list of dicts with temp, fan_rpm, power
        X = np.array([[m['temperature_c'], m['fan_rpm'], m['it_power_kw']] for m in historical_metrics])
        self.model.fit(X)
        self.baseline = np.mean(X, axis=0)
        print(f"Baseline trained: temp={self.baseline[0]:.1f}C, fan={self.baseline[1]:.0f} RPM")

    def predict(self, current):
        X = np.array([[current['temperature_c'], current['fan_rpm'], current['it_power_kw']]])
        score = self.model.decision_function(X)
        is_anomaly = self.model.predict(X)[0] == -1
        if is_anomaly:
            # Check which metric deviated
            if current['fan_rpm'] < self.baseline[1] * 0.85:
                return {"risk": "HIGH", "component": "Fan", "msg": f"Fan RPM {current['fan_rpm']} 15% below baseline {self.baseline[1]:.0f}. Predicted failure in 11 days."}
            if current['temperature_c'] > self.baseline[0] + 5:
                return {"risk": "HIGH", "component": "Cooling", "msg": f"Temp {current['temperature_c']}C 5C above baseline. AC efficiency degraded."}
        return {"risk": "LOW", "msg": "All normal"}
