from django.urls import path
from . import views
from .views import user_login, menu_upload
from .views import user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.starting_page, name= "Homepage"),
    path('menu/', views.menu_page, name='menu'),  # Definisci l'URL
    path('upload-menu/', views.menu_upload, name='menu_upload'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
