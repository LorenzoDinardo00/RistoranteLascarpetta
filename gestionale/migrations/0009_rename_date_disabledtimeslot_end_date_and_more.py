# Generated by Django 5.0.6 on 2024-12-06 11:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0008_disabledtimeslot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disabledtimeslot',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AlterUniqueTogether(
            name='disabledtimeslot',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='disabledtimeslot',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]