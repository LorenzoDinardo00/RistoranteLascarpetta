from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    guests = models.IntegerField(default=1)
    reservation_date = models.DateField()
    reservation_time = models.CharField(max_length=10)  # Mantieni sempre il formato 'HH:MM'
    cookie_consent = models.BooleanField(default=False)
    profiling_consent = models.BooleanField(default=False)
    promotional_sms_consent = models.BooleanField(default=False)
    accept_all = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)  

    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date} {self.reservation_time}"
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    hashtag = models.CharField(max_length=100, blank=True, null=True, default="")
    numero_prenotazioni = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"
  
from django.db import models
# models.py
from django.db import models

class DisabledDate(models.Model):
    date = models.DateField(unique=True, help_text="Date to disable for reservations")
    reason = models.TextField(blank=True, help_text="Optional reason for disabling the date")

    def __str__(self):
        return f"{self.date} - {self.reason}"

from django.db import models

class DisabledTimeSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.start_time} to {self.end_time}"