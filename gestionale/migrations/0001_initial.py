# Generated by Django 5.0.6 on 2024-11-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('guests', models.IntegerField(default=1)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('cookie_consent', models.BooleanField(default=False)),
                ('profiling_consent', models.BooleanField(default=False)),
                ('promotional_sms_consent', models.BooleanField(default=False)),
                ('accept_all', models.BooleanField(default=False)),
            ],
        ),
    ]