from django.db import models

class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_images/')
    description = models.CharField(max_length=255, default='Immagine del Menù')

    def __str__(self):
        return self.description
    

class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
