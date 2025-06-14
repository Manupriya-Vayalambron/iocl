from sklearn.ensemble import IsolationForest
import numpy as np

def detect_wastage(equipment_id):
    records = EnergyRecord.objects.filter(equipment_id=equipment_id)
    power_data = np.array([r.power_usage for r in records]).reshape(-1, 1)
    
    # Train anomaly detector
    clf = IsolationForest(contamination=0.05)  # 5% expected anomalies
    clf.fit(power_data)
    
    # Update records
    for record in records:
        pred = clf.predict([[record.power_usage]])
        record.is_wastage = pred[0] == -1
        if record.is_wastage:
            record.reason = f"Abnormal power draw ({record.power_usage} kW)"
        record.save()