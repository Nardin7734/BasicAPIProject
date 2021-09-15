from generos_e_tipos.models import Generos, Tipos
from rest_framework import serializers
from generos_e_tipos.validators import *


class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'

    def validate(self, data):
        if not nome_e_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras!'})
        return data


class TiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos
        fields = '__all__'

    def validate(self, data):
        if not nome_e_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras!'})
        return data
