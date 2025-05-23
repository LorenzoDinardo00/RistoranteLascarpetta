# Generated by Django 5.0.6 on 2024-12-06 23:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0011_alter_disableddate_date_alter_disableddate_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disableddate',
            name='date',
        ),
        migrations.AddField(
            model_name='disableddate',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disableddate',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
