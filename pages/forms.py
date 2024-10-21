from django import forms
from .models import MenuImage, PDFDocument

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


# La classe PDFUploadForm deve essere fuori dalla classe MenuImageForm
class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.pdf'):
            raise forms.ValidationError("Devi caricare un file PDF.")
        return file