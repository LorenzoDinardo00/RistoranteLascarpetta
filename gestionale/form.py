from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'phone_number', 'guests', 'reservation_date', 'reservation_time', 
                  'cookie_consent', 'profiling_consent', 'promotional_sms_consent', 'accept_all']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_cookie_consent(self):
        cookie_consent = self.cleaned_data.get('cookie_consent')
        if not cookie_consent:
            raise forms.ValidationError("Devi accettare i cookie per prenotare.")
        return cookie_consent