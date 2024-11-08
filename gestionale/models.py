from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    guests = models.IntegerField(default=1)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    cookie_consent = models.BooleanField(default=False)
    profiling_consent = models.BooleanField(default=False)
    promotional_sms_consent = models.BooleanField(default=False)
    accept_all = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date} {self.reservation_time}"