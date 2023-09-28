from rest_framework import serializers
from .models import User, Dado, Sinal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = '__all__'

class SinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinal
        fields = '__all__'