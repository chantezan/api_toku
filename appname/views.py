
from rest_framework.response import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Avg
from django_filters import rest_framework as filters
from .models import Heroe
from .serializer import HeroSerializer, HeroAverageSerializer


class HeroFilter(filters.FilterSet):
    intelligence_greater = filters.NumberFilter(field_name="intelligence", lookup_expr="gte")
    intelligence_less = filters.NumberFilter(field_name="intelligence", lookup_expr="lte")
    strength_greater = filters.NumberFilter(field_name="strength", lookup_expr="gte")
    strength_less = filters.NumberFilter(field_name="strength", lookup_expr="lte")
    speed_greater = filters.NumberFilter(field_name="speed", lookup_expr="gte")
    speed_less = filters.NumberFilter(field_name="speed", lookup_expr="lte")
    durability_greater = filters.NumberFilter(field_name="urability", lookup_expr="gte")
    durability_less = filters.NumberFilter(field_name="durability", lookup_expr="lte")
    power_greater = filters.NumberFilter(field_name="power", lookup_expr="gte")
    power_less = filters.NumberFilter(field_name="power", lookup_expr="lte")
    combat_greater = filters.NumberFilter(field_name="combat", lookup_expr="gte")
    combat_less = filters.NumberFilter(field_name="combat", lookup_expr="lte")
    class Meta:
        model = Heroe
        fields = {
            "alignment": ["exact"],
            "gender": ["exact"],
            "race": ["exact"],
        }

class HeroIntelligenceAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "intelligence"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)

class HeroStrengthAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "strength"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)

class HeroSpeedAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "speed"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)

class HeroDurabilityAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "durability"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)

class HeroPowerAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "power"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)


class HeroCombatAvg(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter
    atribute = "combat"

    @swagger_auto_schema(
        operation_summary="Average " + atribute + " of all heroes",
        operation_description="Calculates the average " + atribute + " of all heroes.",
        responses={
            200: "Average " + atribute
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        filtered_queryset = filtered_queryset.aggregate(average=Avg(self.atribute))
        serializer = HeroAverageSerializer(filtered_queryset)
        return Response(serializer.data)

class HeroApi(generics.GenericAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HeroFilter

    @swagger_auto_schema(
        operation_summary="Return all heroe",
        operation_description="Return all heros in filter.",
        responses={
            200: "Heros"
        }
    )
    def get(self, request):
        queryset = Heroe.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = HeroSerializer(filtered_queryset, many=True)
        return Response(serializer.data)


