# Generated by Django 5.0.6 on 2024-12-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0014_alter_disableddate_date_alter_disableddate_end_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisabledTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='disableddate',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='disableddate',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='date',
            field=models.DateField(help_text='Date to disable for reservations', unique=True),
        ),
        migrations.AlterField(
            model_name='disableddate',
            name='reason',
            field=models.TextField(blank=True, help_text='Optional reason for disabling the date'),
        ),
    ]