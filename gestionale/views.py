from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from twilio.rest import Client
from .form import ReservationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import DisabledDate, Reservation
from .form import ReservationForm
def prenota_tavolo(request):
    """
    Gestisce la prenotazione del tavolo, inclusa la gestione dei consensi,
    l'invio dell'email e l'aggiornamento della lista clienti.
    """
    # Recupera tutte le date disabilitate
    disabled_dates = DisabledDate.objects.values_list('date', 'reason')
    formatted_disabled_dates = [
        {'date': date.strftime("%Y-%m-%d"), 'reason': reason or "Non specificata"} for date, reason in disabled_dates
    ]

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            # Salva la prenotazione
            reservation = form.save(commit=False)
            reservation.reservation_time = reservation.reservation_time.strip()
            reservation.save()

            # Verifica se il consenso alla profilazione è stato accettato
            if form.cleaned_data.get('profiling_consent'):
                customer, created = Customer.objects.get_or_create(
                    phone_number=reservation.phone_number,
                    defaults={
                        'first_name': reservation.first_name,
                        'last_name': reservation.last_name,
                        # Altri valori di default se necessari
                    }
                )
                if not created:
                    # Aggiorna i dati del cliente esistente
                    customer.first_name = reservation.first_name
                    customer.last_name = reservation.last_name
                    customer.save()

            # Invia un'email al titolare
            try:
                send_mail(
                    subject='Nuova Prenotazione - La Scarpetta',
                    message=f"""
Gentile Titolare,

È stata effettuata una nuova prenotazione presso il ristorante La Scarpetta:

- Nome Cliente: {reservation.first_name} {reservation.last_name}
- Telefono Cliente: {reservation.phone_number}
- Data Prenotazione: {reservation.reservation_date.strftime('%d/%m/%Y')}
- Ora Prenotazione: {reservation.reservation_time}
- Numero di Persone: {reservation.guests}

Cordiali saluti,
Il Team di La Scarpetta
""",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['temporainnovation@gmail.com','lascarpettafirenze@gmail.com','artursiko4@gmail.com'],  # Sostituisci con un tuo indirizzo reale
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Errore durante l'invio dell'email: {e}")

            # Redireziona alla pagina di successo
            return redirect(reverse('gestionale:reservation_success'))
        else:
            # Ritorna errori del modulo
            return render(request, 'gestionale/prenota_tavolo.html', {
                'form': form,
                'disabled_dates': formatted_disabled_dates,
            })
    else:
        # Mostra il modulo vuoto
        form = ReservationForm()

    # Rendi il template con il modulo e le date disabilitate
    return render(request, 'gestionale/prenota_tavolo.html', {
        'form': form,
        'disabled_dates': formatted_disabled_dates,
    })
    
def send_confirmation_sms(reservation):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = f"Grazie {reservation.first_name} {reservation.last_name} per la tua prenotazione da La Scarpetta il {reservation.reservation_date} alle {reservation.reservation_time}. A presto!"
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=reservation.phone_number
        )
    except Exception as e:
        print(f"Errore nell'invio dell'SMS: {e}")
        
def reservation_success(request):
    return render(request, 'gestionale/reservation_success.html')




def gestionale(request):
    return render(request, 'gestionale/gestionale.html')
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Reservation
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Reservation
@login_required
def prenotazioni(request):
    # Ottieni la data selezionata dal parametro GET, con default alla data odierna
    selected_date_str = request.GET.get('date', timezone.now().date().isoformat())
    selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    
    # Recupera le prenotazioni per la data selezionata, ordinate per orario
    reservations = Reservation.objects.filter(reservation_date=selected_date).order_by('reservation_time')
    
    # Suddividi le prenotazioni in pranzo e cena
    lunch_reservations = reservations.filter(reservation_time__lt="15:00")
    dinner_reservations = reservations.filter(reservation_time__gte="15:00")
    
    # Calcola le date precedente e successiva per la navigazione
    prev_date = (selected_date - timedelta(days=1)).isoformat()
    next_date = (selected_date + timedelta(days=1)).isoformat()
    
    context = {
        'selected_date': selected_date,
        'lunch_reservations': lunch_reservations,
        'dinner_reservations': dinner_reservations,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    
    return render(request, 'gestionale/prenotazioni.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Reservation
def prenotazione_dettaglio(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'gestionale/prenotazione_dettaglio.html', {'reservation': reservation})


from .models import Customer

from django.db.models import Value
from django.db.models.functions import Concat

@login_required
def clienti(request):
    customers = Customer.objects.all().order_by('last_name', 'first_name')
    hashtags = (
        Customer.objects
        .exclude(hashtag="")
        .values_list('hashtag', flat=True)
    )
    # Dividi gli hashtag in una lista univoca
    unique_hashtags = set(tag.strip() for tags in hashtags for tag in tags.split(',') if tag.strip())
    return render(request, 'gestionale/clienti.html', {
        'customers': customers,
        'unique_hashtags': unique_hashtags,
    })
    
def statistiche(request):
    return render(request, 'gestionale/statistiche.html')

def report(request):
    return render(request, 'gestionale/report.html')

from django.shortcuts import render
@login_required
def update_hashtag(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        hashtag = request.POST.get('hashtag', '').strip()
        customer.hashtag = hashtag
        customer.save()
    return redirect(reverse('gestionale:clienti'))


@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect(reverse('gestionale:clienti'))


from django.db.models import Q

from django.db.models import Q
from django.db.models import Q
from django.shortcuts import render  # Assicurati che sia importato
from django.contrib.auth.decorators import login_required
from .models import Customer

@login_required
def search_customers_by_hashtag(request):
    hashtag_query = request.GET.get('hashtag', '').strip()
    if hashtag_query:
        customers = Customer.objects.filter(hashtag__icontains=hashtag_query)
    else:
        customers = Customer.objects.all()

    hashtags = (
        Customer.objects
        .exclude(hashtag="")
        .values_list('hashtag', flat=True)
    )
    unique_hashtags = set(tag.strip() for tags in hashtags for tag in tags.split(',') if tag.strip())

    return render(request, 'gestionale/search_customers.html', {
        'customers': customers,
        'hashtag_query': hashtag_query,
        'unique_hashtags': unique_hashtags,
    })
    
from django.contrib.auth.decorators import login_required
from .models import Customer
# from twilio.rest import Client
# from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
@login_required
def send_sms(request):
    selected_customer_ids = request.POST.getlist('selected_customers')  # Ottieni gli ID dei clienti selezionati
    search_query = request.GET.get('search', '').strip()  # Ottieni il termine di ricerca, se presente

    # Recupera i clienti selezionati
    selected_customers = Customer.objects.filter(id__in=selected_customer_ids)

    # Recupera i risultati della ricerca
    search_results = Customer.objects.filter(
        first_name__icontains=search_query
    ) | Customer.objects.filter(
        last_name__icontains=search_query
    ) if search_query else []

    if request.method == 'POST' and 'send_sms' in request.POST:
        # Invio degli SMS
        message = request.POST.get('message', '')
        for customer in selected_customers:
            if customer.phone_number:
                # Simulazione di invio SMS (Twilio commentato)
                print(f"SMS simulato inviato a {customer.phone_number} con messaggio: {message}")
        return redirect('gestionale:sms_success')

    return render(request, 'gestionale/sms_sender.html', {
        'selected_customers': selected_customers,
        'search_results': search_results,
        'search_query': search_query,
    })
# Funzione per inviare SMS tramite Twilio (commentata per ora)
# def send_sms_to_customer(phone_number, message):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     client.messages.create(
#         body=message,
#         from_=settings.TWILIO_SENDER_ID,
#         to=phone_number
#     )

@login_required
def sms_success(request):
    return render(request, 'gestionale/sms_success.html')

from django.shortcuts import get_object_or_404, redirect, render
from .models import Reservation
@login_required
def modifica_prenotazione(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    valid_times = [
        "12:00", "12:30", "13:00", "13:30", "14:00",
        "19:00", "19:30", "20:00", "20:30", "21:00",
        "21:30", "22:00", "22:30", "23:00"
    ]

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('gestionale:prenotazioni')  # Sostituisci con la tua URL di successo
        else:
            print(form.errors)  # Debug: Mostra errori di validazione
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'gestionale/modifica_prenotazione.html', {
        'form': form,
        'reservation': reservation,
        'valid_times': valid_times
    })
    
@login_required
def elimina_prenotazione(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('gestionale:prenotazioni')
    return render(request, 'gestionale/elimina_prenotazione.html', {'reservation': reservation})

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation

@login_required
def elimina_tutte_prenotazioni(request):
    if request.method == 'POST':
        # Cancella tutte le prenotazioni
        Reservation.objects.all().delete()
        messages.success(request, "Tutte le prenotazioni sono state eliminate con successo.")
        return redirect('gestionale:prenotazioni')  # Reindirizza alla lista delle prenotazioni
    
    # Mostra una pagina di conferma
    return render(request, 'gestionale/elimina_tutte.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import DisabledDate
from .form import DisabledDateForm
from datetime import timedelta
@login_required
def manage_disabled_dates(request):
    if request.method == 'POST':
        form = DisabledDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            reason = form.cleaned_data.get('reason')

            # Aggiungi tutte le date nell'intervallo specificato
            current_date = start_date
            while current_date <= end_date:
                DisabledDate.objects.get_or_create(date=current_date, defaults={'reason': reason})
                current_date += timedelta(days=1)

            return redirect('gestionale:manage_disabled_dates')

    else:
        form = DisabledDateForm()

    # Recupera tutte le date disabilitate, inclusi gli ID
    disabled_dates = DisabledDate.objects.all()  # Recupera tutti gli oggetti completi

    return render(request, 'gestionale/manage_disabled_dates.html', {
        'form': form,
        'disabled_dates': disabled_dates,  # Passa oggetti completi con `id`
    })
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import DisabledDate
@login_required
def delete_disabled_date(request, pk):
    """
    Rimuove una data disabilitata identificata dalla chiave primaria (pk).
    """
    if request.method == 'POST':
        disabled_date = get_object_or_404(DisabledDate, pk=pk)
        disabled_date.delete()
        return redirect('gestionale:manage_disabled_dates')
    return HttpResponse(status=405)  # Metodo non consentito

from django.core.mail import send_mail
from django.http import HttpResponse
import logging
from django.core.mail import send_mail
from django.http import HttpResponse
import logging

# Configura il logger
logger = logging.getLogger(__name__)

def test_email(request):
    """
    Simula l'invio di una email per verificare che il servizio di posta funzioni correttamente con SendGrid.
    """
    try:
        logger.info("Tentativo di invio email di test tramite SendGrid.")
        send_mail(
            subject='Test Email - La Scarpetta',
            message='Questa è una email di prova inviata dal sistema di prenotazione La Scarpetta.',
            from_email='assistenza.lorenzodinardo@gmail.com',  # Mittente verificato in SendGrid
            recipient_list=['lorenzodinardo030@gmail.com','lascarpettafirenze@gmail.com','artursiko4@gmail.com'],  # Sostituisci con un tuo indirizzo reale
            fail_silently=False,
        )
        logger.info("Email di test inviata con successo.")
        return HttpResponse("Email di test inviata con successo!")
    except Exception as e:
        logger.error(f"Errore durante l'invio dell'email di test: {e}")
        return HttpResponse(f"Errore durante l'invio dell'email di test: {e}")
    
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import DisabledDate, DisabledTimeSlot, Reservation, Customer
from .form import ReservationForm, DisabledDateForm, DisabledTimeSlotForm
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from datetime import datetime, timedelta   
@login_required
def manage_disabled_time_slots(request):
    # Lista di orari preimpostati
    time_slots = [
        "12:00", "12:30", "13:00", "13:30", "14:00",
        "19:00", "19:30", "20:00", "20:30", "21:00",
        "21:30", "22:00", "22:30", "23:00", "23:59"
    ]

    if request.method == "POST":
        form = DisabledTimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionale:manage_disabled_time_slots')
    else:
        form = DisabledTimeSlotForm()

    # Recupera tutte le fasce orarie disabilitate
    disabled_time_slots = DisabledTimeSlot.objects.all()

    return render(request, 'gestionale/manage_disabled_time_slots.html', {
        'form': form,
        'disabled_time_slots': disabled_time_slots,
        'time_slots': time_slots,  # Passa gli orari preimpostati al template
    })


@login_required
def delete_disabled_time_slot(request, pk):
    slot = get_object_or_404(DisabledTimeSlot, pk=pk)
    if request.method == "POST":
        slot.delete()
        return redirect('gestionale:manage_disabled_time_slots') 
    
from django.http import JsonResponse
from .models import DisabledTimeSlot


def get_disabled_time_slots(request):
    date = request.GET.get('date')
    if date:
        disabled_slots = DisabledTimeSlot.objects.filter(date=date)
        data = {
            'disabled_time_slots': [
                {'start_time': slot.start_time.strftime('%H:%M'), 'end_time': slot.end_time.strftime('%H:%M')}
                for slot in disabled_slots
            ]
        }
    else:
        data = {'disabled_time_slots': []}
    return JsonResponse(data)