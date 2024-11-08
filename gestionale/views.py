from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from twilio.rest import Client
from .form import ReservationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def prenota_tavolo(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            
            # Invia l'SMS di conferma con Twilio solo se i cookie sono stati accettati
            if reservation.phone_number and reservation.cookie_consent:
                # send_confirmation_sms(reservation)
                pass  # Commentato temporaneamente per evitare l'invio di SMS
            return redirect(reverse('gestionale:reservation_success'))
    else:
        form = ReservationForm()
    return render(request, 'gestionale/prenota_tavolo.html', {'form': form})

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

def prenotazioni(request):
    # Ottieni la data selezionata dal parametro GET, con default alla data odierna
    selected_date_str = request.GET.get('date', timezone.now().date().isoformat())
    selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    
    # Recupera le prenotazioni per la data selezionata, ordinate per orario
    reservations = Reservation.objects.filter(reservation_date=selected_date).order_by('reservation_time')
    
    # Suddividi le prenotazioni in pranzo e cena
    lunch_reservations = reservations.filter(reservation_time__lt=datetime.strptime('15:00', '%H:%M').time())
    dinner_reservations = reservations.filter(reservation_time__gte=datetime.strptime('15:00', '%H:%M').time())
    
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
    try:
        # Recupera la prenotazione o mostra un errore 404 se non esiste
        reservation = get_object_or_404(Reservation, id=reservation_id)
    except Reservation.DoesNotExist:
        # Gestisce il caso in cui l'ID non corrisponda ad alcuna prenotazione
        return render(request, 'gestionale/prenotazione_dettaglio.html', {
            'error': 'Prenotazione non trovata.'
        })
    
    context = {
        'reservation': reservation,
    }
    
    return render(request, 'gestionale/prenotazione_dettaglio.html', context)

def clienti(request):
    return render(request, 'gestionale/clienti.html')

def statistiche(request):
    return render(request, 'gestionale/statistiche.html')

def report(request):
    return render(request, 'gestionale/report.html')