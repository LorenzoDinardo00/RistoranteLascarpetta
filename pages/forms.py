from django import forms
from .models import MenuImage

class MenuImageForm(forms.ModelForm):
    class Meta:
        model = MenuImage
        fields = ['image']