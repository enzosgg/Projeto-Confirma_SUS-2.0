from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('sus.urls')),
    path('', include('sus_medicos.urls')),
    path('', include('recepcao.urls')),
    path('', include('sus_medicos.urls')),
]