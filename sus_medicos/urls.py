from django.urls import path
from . import views

urlpatterns = [
    path('plataforma_medico/', views.plataforma_medico, name='plataforma_medico'),
    path('consulta_medico/<int:id>/', views.consulta_medico, name='consulta_medico'),
    path('paciente_compareceu/<int:id>/', views.paciente_compareceu, name='paciente_compareceu'),
    path('paciente_nao_compareceu/<int:id>/', views.paciente_nao_compareceu, name='paciente_nao_compareceu'),
    path('logout_medico', views.logout_medico, name='logout_medico'),
]