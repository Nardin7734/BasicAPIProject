from rest_framework import viewsets
from midias.models import Midias
from midias.serializers import MidiasSerializers
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class MidiasViewSet(viewsets.ModelViewSet):
    queryset = Midias.objects.all()
    serializer_class = MidiasSerializers
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
