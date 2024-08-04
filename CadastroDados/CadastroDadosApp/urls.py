
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('enviar_dados/', views.enviar_dados, name='enviar_dados'),
    path('dados/', views.dados, name='dados'),
]