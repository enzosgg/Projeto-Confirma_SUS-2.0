from .views import gerar_estatisticas
from django.urls import path

urlpatterns = [
    path('gerar_estatisticas/', gerar_estatisticas, name='gerar_estatisticas'),
]