from django.db import models

class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_images/')
    description = models.CharField(max_length=255, default='Immagine del Menù')

    def __str__(self):
        return self.description