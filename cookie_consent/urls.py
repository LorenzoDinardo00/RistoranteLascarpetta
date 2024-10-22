from . import views
from django.urls import path, include

from django.urls import path
from . import views
app_name = 'cookie_consent'

urlpatterns = [
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),

    
]