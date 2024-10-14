from django import forms
from .models import MenuImage

class MenuImageForm(forms.ModelForm):
    class Meta:
        model = MenuImage
        fields = ['image', 'description']
        widgets = {
            'description': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(MenuImageForm, self).__init__(*args, **kwargs)
        self.fields['description'].initial = 'Immagine del Menù'