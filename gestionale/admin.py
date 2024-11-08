from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'guests', 'reservation_date', 'reservation_time')