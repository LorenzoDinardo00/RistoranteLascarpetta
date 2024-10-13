from django.contrib import admin
from .models import MenuImage
from django.contrib import messages

# Register your models here.
@admin.register(MenuImage)
class MenuImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'description']
    # Override del metodo di eliminazione singola
    def delete_model(self, request, obj):
        # Puoi aggiungere logica personalizzata qui prima di eliminare l'elemento
        obj.delete()
        self.message_user(request, "L'immagine è stata eliminata con successo", messages.SUCCESS)

    # Override per l'eliminazione di più oggetti
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Logica personalizzata per ogni oggetto eliminato
            obj.delete()
        self.message_user(request, "Le immagini selezionate sono state eliminate con successo", messages.SUCCESS)