from django.urls import path
from . import views
from .views import user_login, menu_upload
from .views import user_logout
from django.conf import settings
from .views import prenotazioni
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path("", views.starting_page, name= "Homepage"),
    path('menu/', views.menu_page, name='menu'),  # Definisci l'URL
    path('upload-menu/', views.menu_upload, name='menu_upload'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('prenotazioni/', prenotazioni, name='prenotazioni'),
    path('create-superuser/', views.create_superuser, name='create_superuser'),
    path('pdf/upload/', views.upload_pdf, name='upload_pdf'),     # Caricamento PDF
    path('', include('cookie_consent.urls')), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)