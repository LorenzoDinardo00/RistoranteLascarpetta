from . import views
from django.urls import path, include

urlpatterns = [
    path('manage-cookies/', manage_cookies, name='manage_cookies'),
]