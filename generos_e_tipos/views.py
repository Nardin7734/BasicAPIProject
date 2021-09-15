from rest_framework import viewsets
from .serializers import GenerosSerializer, TiposSerializer
from .models import Generos, Tipos


class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer


class TiposViewSet(viewsets.ModelViewSet):
    queryset = Tipos.objects.all()
    serializer_class = TiposSerializer
