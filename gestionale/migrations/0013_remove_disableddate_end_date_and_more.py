# Generated by Django 5.0.6 on 2024-12-07 00:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0012_remove_disableddate_date_disableddate_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disableddate',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='disableddate',
            name='start_date',
        ),
        migrations.AddField(
            model_name='disableddate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Date to disable for reservations', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='end_time',
            field=models.TimeField(blank=True, help_text='Orario di fine indisponibilità', null=True),
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='reason',
            field=models.TextField(blank=True, help_text='Optional reason for disabling the date'),
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='start_time',
            field=models.TimeField(blank=True, help_text='Orario di inizio indisponibilità', null=True),
        ),
    ]