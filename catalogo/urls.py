"""catalogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from midias.views import MidiasViewSet
from generos_e_tipos.views import GenerosViewSet, TiposViewSet

router = routers.DefaultRouter()
router.register('generos', GenerosViewSet, basename='Generos')
router.register('midias', MidiasViewSet, basename='Midias')
router.register('tipos', TiposViewSet, basename='Tipos')


urlpatterns = [
    path('onizuka/', admin.site.urls),
    path('', include(router.urls)),
]
