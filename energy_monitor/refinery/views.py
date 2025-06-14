from django.shortcuts import render
from .models import EnergyRecord

def dashboard_view(request):
    wastage_records = EnergyRecord.objects.filter(is_wastage=True).order_by('-timestamp')[:10]
    
    timestamps = [r.timestamp.strftime("%Y-%m-%d %H:%M") for r in EnergyRecord.objects.all()]
    power_data = [r.power_usage for r in EnergyRecord.objects.all()]

    return render(request, 'refinery/dashboard.html', {
        'wastage_records': wastage_records,
        'timestamps': timestamps,
        'power_data': power_data
    })
