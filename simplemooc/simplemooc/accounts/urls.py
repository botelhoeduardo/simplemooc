from django.urls import path
from django.contrib.auth import login

app_name = 'accounts'

urlpatterns = [
    path('entrar/', login,
    {'template_name' : 'accounts/login.html'} , name='login')
]