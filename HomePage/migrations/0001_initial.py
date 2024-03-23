# Generated by Django 5.0.3 on 2024-03-23 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AirLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_airport', models.CharField(max_length=20)),
                ('to_airport', models.CharField(max_length=20)),
                ('from_city', models.CharField(max_length=10)),
                ('to_city', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_airport', models.CharField(max_length=20)),
                ('to_airport', models.CharField(max_length=20)),
                ('departure_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('flight_num', models.CharField(max_length=10)),
                ('departure_time', models.DateTimeField()),
                ('return_time', models.DateTimeField()),
                ('company', models.CharField(default=' ', max_length=30)),
                ('seats', models.IntegerField()),
                ('location', models.ManyToManyField(to='HomePage.location')),
                ('passengers', models.ManyToManyField(related_name='flights', to='HomePage.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takeoff_date', models.DateTimeField(auto_now_add=True)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ticket_class', models.CharField(choices=[('economy', 'Economy'), ('economy_plus', 'Economy Plus'), ('business', 'Business'), ('vip', 'VIP')], max_length=15)),
                ('seat_number', models.IntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.flight')),
                ('passenger', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_passenger', to='HomePage.passenger')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='ticket',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passenger_ticket', to='HomePage.ticket'),
        ),
        migrations.AddField(
            model_name='flight',
            name='tickets',
            field=models.ManyToManyField(related_name='flights', to='HomePage.ticket'),
        ),
    ]
