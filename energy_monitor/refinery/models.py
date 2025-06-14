from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)  # e.g., "CDU Pump-3"
    normal_power_range = models.CharField(max_length=50)  # "80-150 kW"

class EnergyRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    power_usage = models.FloatField()  # in kW
    is_wastage = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, blank=True)