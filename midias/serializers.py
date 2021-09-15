from midias.models import Midias
from rest_framework import serializers
from midias.validators import *


class MidiasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Midias
        fields = ['id', 'nome', 'genero', 'tipo', 'lancamento', 'nota', 'descricao']

    def validate(self, data):
        if not nota_e_valida(data['nota']):
            raise serializers.ValidationError({'nota': 'A nota deve ser maior que -1 e menor que 11!'})
        return data

