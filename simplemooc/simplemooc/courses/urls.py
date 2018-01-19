from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='index'),
    # path('<int:pk>/', views.details, name='details')
    path('<slug>', views.details, name='details')
]