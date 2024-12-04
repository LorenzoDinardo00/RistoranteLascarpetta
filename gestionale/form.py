from django import forms
from .models import Reservation
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
    def clean_reservation_date(self):
        """
        Verifica che la data della prenotazione non sia in un giorno disabilitato.
        """
        reservation_date = self.cleaned_data.get('reservation_date')

        # Controlla se la data è disabilitata
        from .models import DisabledDate
        if DisabledDate.objects.filter(date=reservation_date).exists():
            raise forms.ValidationError("La data selezionata non è disponibile per le prenotazioni.")

        return reservation_date

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

    from django import forms
from .models import Reservation

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
def clean_cookie_consent(self):
        cookie_consent = self.cleaned_data.get('cookie_consent')
        if not cookie_consent:
            raise forms.ValidationError("Devi accettare i cookie per prenotare.")
        return cookie_consent
    



from django import forms
from .models import DisabledDate

class DisabledDateForm(forms.ModelForm):
    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Seleziona la data di inizio"
    )
    end_date = forms.DateField(
        required=False,  # Non obbligatoria lato form, verrà gestita dal backend
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

        # Imposta end_date uguale a start_date se non è stato fornito
        if not end_date:
            end_date = start_date
            cleaned_data['end_date'] = end_date

        # Verifica che start_date <= end_date
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("La data di inizio non può essere successiva alla data di fine.")

        return cleaned_data