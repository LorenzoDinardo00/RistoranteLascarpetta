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