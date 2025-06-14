from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EnergyRecord

@receiver(post_save, sender=EnergyRecord)
def send_wastage_alert(sender, instance, **kwargs):
    if instance.is_wastage:
        subject = f"Energy Wastage Alert: {instance.equipment.name}"
        message = f"""
        Abnormal energy consumption detected!
        
        Equipment: {instance.equipment.name}
        Power Usage: {instance.power_usage} kW
        Time: {instance.timestamp}
        Reason: {instance.reason}
        """
        send_mail(
            subject,
            message,
            'alerts@refinerymonitor.com',
            ['plant.manager@iocl.com'],
            fail_silently=False,
        )