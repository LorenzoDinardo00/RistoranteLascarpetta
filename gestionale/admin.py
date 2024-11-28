from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'guests', 'reservation_date', 'reservation_time')
    
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'hashtag', 'numero_prenotazioni')
    search_fields = ('first_name', 'last_name', 'phone_number')