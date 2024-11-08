from django.urls import path
from . import views

app_name = 'gestionale'  # Definisci il namespace

urlpatterns = [
    path('prenota/', views.prenota_tavolo, name='reservation'),  # Associa 'reservation' alla vista 'prenota_tavolo'
    path('prenota-tavolo/', views.prenota_tavolo, name='prenota_tavolo'),  # Nome del path corrispondente
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('', views.gestionale, name='gestionale'),
    path('prenotazioni/', views.prenotazioni, name='prenotazioni'),
    path('clienti/', views.clienti, name='clienti'),
    path('statistiche/', views.statistiche, name='statistiche'),
    path('report/', views.report, name='report'),
    path('prenotazioni/<int:reservation_id>/', views.prenotazione_dettaglio, name='prenotazione_dettaglio'),

]