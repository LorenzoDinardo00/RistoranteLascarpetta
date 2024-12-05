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
    path('clienti/<int:customer_id>/update/', views.update_hashtag, name='update_hashtag'),
    path('clienti/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('clienti/ricerca/', views.search_customers_by_hashtag, name='search_customers_by_hashtag'),
     # Rotta per la vista di invio SMS
    path('send-sms/', views.send_sms, name='send_sms'),
    # Rotta per la conferma di invio SMS (success page)
    path('sms-success/', views.sms_success, name='sms_success'),
    path('clienti/<int:customer_id>/update/', views.update_hashtag, name='update_hashtag'),
    path('modifica/<int:reservation_id>/', views.modifica_prenotazione, name='modifica_prenotazione'),
    path('elimina/<int:reservation_id>/', views.elimina_prenotazione, name='elimina_prenotazione'),
    path('prenotazioni/elimina_tutte/', views.elimina_tutte_prenotazioni, name='elimina_tutte_prenotazioni'),
    path('manage-disabled-dates/', views.manage_disabled_dates, name='manage_disabled_dates'),
    path('delete-disabled-date/<int:pk>/', views.delete_disabled_date, name='delete_disabled_date'),
    path('test-email/', views.test_email, name='test_email'),

]