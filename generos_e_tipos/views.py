from rest_framework import viewsets
from .serializers import GenerosSerializer, TiposSerializer
from .models import Generos, Tipos
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    http_method_names = ['get', 'post', 'put', 'patch']


class TiposViewSet(viewsets.ModelViewSet):
    queryset = Tipos.objects.all()
    serializer_class = TiposSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    http_method_names = ['get', 'post', 'put', 'patch']


