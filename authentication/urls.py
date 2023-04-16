# authentication/urls.py

from django.urls import path
from .views import token_obtain_pair, token_refresh

urlpatterns = [
    path('login/', token_obtain_pair, name='login'),
    path('refresh/', token_refresh, name='refresh'),
]
