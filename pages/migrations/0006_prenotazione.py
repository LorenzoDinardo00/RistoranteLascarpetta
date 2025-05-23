# Generated by Django 5.0.6 on 2024-11-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_pdfdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prenotazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=15)),
                ('persone', models.IntegerField()),
                ('data', models.DateField()),
                ('ora', models.TimeField()),
                ('cookie_consent', models.BooleanField(default=False)),
                ('data_profilazione', models.BooleanField(default=False)),
                ('promozioni_sms', models.BooleanField(default=False)),
            ],
        ),
    ]
