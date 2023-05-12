from rest_framework import serializers
from .models import Heroe

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroe
        fields = ['id_external', 'name']

class HeroAverageSerializer(serializers.Serializer):
    average = serializers.FloatField()