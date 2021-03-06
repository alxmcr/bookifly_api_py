# Generated by Django 3.2.6 on 2021-10-31 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityId', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flightId', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('departure', models.TimeField(verbose_name='Departure')),
                ('arrival', models.TimeField(verbose_name='Arrival')),
                ('duration', models.TimeField(verbose_name='Duration')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('flight_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_from', to='api.city')),
                ('flight_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_to', to='api.city')),
            ],
        ),
    ]
