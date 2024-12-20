# Generated by Django 5.0.6 on 2024-12-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0005_alter_reservation_reservation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisabledDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Date to disable for reservations', unique=True)),
                ('reason', models.TextField(blank=True, help_text='Optional reason for disabling the date')),
            ],
        ),
    ]
