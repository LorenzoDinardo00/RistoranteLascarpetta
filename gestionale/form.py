# forms.py
from django import forms
from .models import Reservation, DisabledDate, DisabledTimeSlot

class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'inputmode': 'none',
            'class': 'form-control',
        })
    )

    reservation_time = forms.TimeField(
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    
    def __init__(self, *args, **kwargs):
        is_restaurateur = kwargs.pop('is_restaurateur', False)
        super().__init__(*args, **kwargs)

        # Opzioni per gli orari disponibili
        TIME_CHOICES = [
            ("12:00", "12:00"), ("12:30", "12:30"), ("13:00", "13:00"),
            ("13:30", "13:30"), ("14:00", "14:00"), ("19:00", "19:00"),
            ("19:30", "19:30"), ("20:00", "20:00"), ("20:30", "20:30"),
            ("21:00", "21:00"), ("21:30", "21:30"), ("22:00", "22:00"),
            ("22:30", "22:30"), ("23:00", "23:00"),
        ]
        self.fields['reservation_time'].widget = forms.Select(
            choices=TIME_CHOICES,
            attrs={'class': 'form-control'}
        )

        # Disabilita i checkbox se il ristoratore accede
        if is_restaurateur:
            for field in ['cookie_consent', 'profiling_consent', 'promotional_sms_consent', 'accept_all']:
                self.fields[field].widget.attrs['disabled'] = True

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data.get('reservation_date')
        if DisabledDate.objects.filter(date=reservation_date).exists():
            raise forms.ValidationError("La data selezionata non è disponibile per le prenotazioni.")
        return reservation_date

    def clean_reservation_time(self):
        reservation_time = self.cleaned_data.get('reservation_time')
        reservation_date = self.cleaned_data.get('reservation_date')
        if reservation_date and reservation_time:
            disabled_slots = DisabledTimeSlot.objects.filter(date=reservation_date)
            for slot in disabled_slots:
                if slot.start_time <= reservation_time < slot.end_time:
                    raise forms.ValidationError(f"L'orario selezionato ({reservation_time}) è disabilitato: {slot.reason or 'Nessuna ragione specificata.'}")
        return reservation_time

    def clean_cookie_consent(self):
        cookie_consent = self.cleaned_data.get('cookie_consent')
        if not cookie_consent:
            raise forms.ValidationError("Devi accettare i cookie per prenotare.")
        return cookie_consent

    class Meta:
        model = Reservation
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'guests',
            'reservation_date',
            'reservation_time',
            'cookie_consent',
            'profiling_consent',
            'promotional_sms_consent',
            'accept_all',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class DisabledDateForm(forms.ModelForm):
    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Seleziona la data di inizio"
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Seleziona la data di fine (opzionale, si autocompila con la data di inizio)"
    )

    class Meta:
        model = DisabledDate
        fields = ['reason']  # La ragione rimane opzionale

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Se end_date non è fornito, impostalo uguale a start_date
        if not end_date:
            cleaned_data['end_date'] = start_date

        # Verifica che start_date sia prima o uguale a end_date
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("La data di inizio non può essere successiva alla data di fine.")

        return cleaned_data

class DisabledTimeSlotForm(forms.ModelForm):
    class Meta:
        model = DisabledTimeSlot
        fields = ['date', 'start_time', 'end_time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
        }