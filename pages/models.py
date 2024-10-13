from django.db import models

class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_images/')  # Campo immagine
    description = models.TextField()  # Puoi avere altri campi per la descrizione, ecc.