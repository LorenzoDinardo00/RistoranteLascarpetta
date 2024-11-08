from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MenuImageForm, PDFUploadForm
from .models import MenuImage, PDFDocument

# View per la homepage: mostra l'ultima immagine e PDF caricati e i form per caricarne di nuovi
def starting_page(request):
    # Inizializzazione dei form
    form_image = MenuImageForm()
    form_pdf = PDFUploadForm()

    # Recupera l'ultima immagine e PDF caricati
    latest_image = MenuImage.objects.last()
    latest_pdf = PDFDocument.objects.last()

    # Passa i form e gli oggetti al template per il rendering
    return render(request, "pages/Homepage.html", {
        'form_image': form_image,
        'form_pdf': form_pdf,
        'latest_image': latest_image,
        'latest_pdf': latest_pdf
    })

def menu_upload(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            # Gestione del caricamento del PDF
            form_pdf = PDFUploadForm(request.POST, request.FILES)
            if form_pdf.is_valid():
                # Elimina tutti i PDF esistenti e i relativi file
                old_pdfs = PDFDocument.objects.all()
                for pdf in old_pdfs:
                    pdf.file.delete(save=False)  # Elimina il file dal filesystem
                    pdf.delete()  # Elimina l'istanza dal database

                # Salva il nuovo PDF
                form_pdf.save()
                return redirect('Homepage')  # Redirigi alla homepage dopo il caricamento
    # Se il metodo è GET o il form non è valido, renderizza la homepage
    form_image = MenuImageForm()
    form_pdf = PDFUploadForm()
    latest_image = MenuImage.objects.last()
    latest_pdf = PDFDocument.objects.last()
    return render(request, 'pages/Homepage.html', {
        'form_image': form_image,
        'form_pdf': form_pdf,
        'latest_image': latest_image,
        'latest_pdf': latest_pdf
    })

# View per la pagina del menu (da personalizzare)
def menu_page(request):
    return render(request, 'pages/Menu.html')  # Assicurati che il percorso del template sia corretto
from django.urls import reverse

# View per gestire il login dell'utente
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Controlla quale pulsante è stato premuto
            if 'login_gestionale' in request.POST:
                # Redirige alla pagina del gestionale se il pulsante "Accedi e vai al gestionale" è stato cliccato
                return redirect('/gestionale/')  # Inserisci l'URL della pagina gestionale
            else:
                # Redirige alla homepage se il pulsante normale di login è stato cliccato
                return redirect('Homepage')
        else:
            # In caso di credenziali non valide
            return render(request, 'pages/Login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'pages/Login.html')
# View per gestire il logout
def user_logout(request):
    logout(request)
    return redirect('Homepage')

# View per la pagina di prenotazione
def prenotazioni(request):
    return render(request, 'pages/prenotazioni.html')

# View per creare un superuser (solo per testing, da rimuovere in produzione)
def create_superuser(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password123')
        return HttpResponse("Superuser creato con successo.")
    else:
        return HttpResponse("Il superuser esiste già.")

# View per il caricamento dei PDF
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})