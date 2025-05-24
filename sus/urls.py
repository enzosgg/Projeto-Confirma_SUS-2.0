from django.urls import path
from . import views

urlpatterns = [
    path('plataforma/', views.plataforma, name='plataforma'),
    path('marcar_consulta/', views.marcar_consulta, name='marcar_consulta'),
    path('confirmar_marcacao/<int:consulta_id>/', views.confirmar_marcacao, name='confirmar_marcacao'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout, name='logout'),
    path('consulta/<int:id>/', views.consulta, name='consulta'),
    path('confirmar_consulta/<int:consulta_id>/', views.confirmar_consulta, name='confirmar_consulta'),
    path('cancelar_consulta/<int:id>/', views.cancelar_consulta, name='cancelar_consulta'),
    path('reagendar/<int:id>/', views.reagendar, name='reagendar'),
    path('confirmar-reagendamento/<int:consulta_atual_id>/<int:nova_consulta_id>/', views.confirmar_reagendamento, name='confirmar_reagendamento')
] 