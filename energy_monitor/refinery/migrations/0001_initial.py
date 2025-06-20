# Generated by Django 4.2.22 on 2025-06-05 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('normal_power_range', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EnergyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('power_usage', models.FloatField()),
                ('is_wastage', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, max_length=200)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refinery.equipment')),
            ],
        ),
    ]
