# Generated by Django 5.0.6 on 2024-12-08 11:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0016_alter_disabledtimeslot_reason'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disabledtimeslot',
            options={'ordering': ['date', 'start_time']},
        ),
        migrations.AlterField(
            model_name='disabledtimeslot',
            name='date',
            field=models.DateField(help_text='Date for which the time slot is disabled'),
        ),
        migrations.AlterField(
            model_name='disabledtimeslot',
            name='end_time',
            field=models.TimeField(help_text='End time of the disabled slot'),
        ),
        migrations.AlterField(
            model_name='disabledtimeslot',
            name='reason',
            field=models.TextField(blank=True, default=django.utils.timezone.now, help_text='Optional reason for disabling the time slot'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disabledtimeslot',
            name='start_time',
            field=models.TimeField(help_text='Start time of the disabled slot'),
        ),
        migrations.AlterUniqueTogether(
            name='disabledtimeslot',
            unique_together={('date', 'start_time', 'end_time')},
        ),
    ]