from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('premierver.urls')),  # Inclure les URLs de l'application
    # Autres URLs globales...
]

