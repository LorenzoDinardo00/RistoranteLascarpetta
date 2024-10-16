from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import MenuImageForm
from .models import MenuImage
from django.contrib.auth import logout

# Create your views here.
def starting_page(request):
    form = MenuImageForm()
    latest_image = MenuImage.objects.last()  # Recupera l'ultima immagine caricata
    return render(request, "pages/Homepage.html", {'form': form, 'latest_image': latest_image})

def menu_page(request):
    return render(request, 'pages/Menu.html')  # Assicurati che il percorso sia corretto

def menu_upload(request):
    if request.method == 'POST':
        form = MenuImageForm(request.POST, request.FILES)  # Gestisci `request.FILES` per i file
        if form.is_valid():
            # Elimina le immagini vecchie, se necessario
            old_images = MenuImage.objects.all()
            for image in old_images:
                # Elimina l'immagine dal backend di storage (es. S3)
                image.image.delete(save=False)  # Elimina dal backend S3 senza salvare il modello
                image.delete()  # Elimina l'istanza dal database

            # Salva la nuova immagine
            form.save()
            return redirect('Homepage')  # Redirigi alla homepage dopo il caricamento
        else:
            print("Errori nel form:", form.errors)  # Debug per errori di validazione
    else:
        form = MenuImageForm()

    # Renderizza la homepage, con il form per caricare l'immagine
    latest_image = MenuImage.objects.last()  # Recupera l'ultima immagine caricata
    return render(request, 'pages/Homepage.html', {'form': form, 'latest_image': latest_image})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Homepage')  # Assicurati che 'homepage' sia configurato correttamente nelle URL
        else:
            return render(request, 'pages/Login.html', {'error': 'Invalid username or password'})
    return render(request, 'pages/Login.html')


def user_logout(request):
    logout(request)
    return redirect('Homepage')


def prenotazioni(request):
    return render(request, 'pages/prenotazioni.html')
