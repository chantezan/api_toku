"""
URL configuration for super_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from appname import views
from django.contrib.staticfiles import views as views_static
from django.urls import re_path

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API Documentation using Swagger",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('heros/', views.HeroApi.as_view(), name="heros"),
    path('avg-intelligence/', views.HeroIntelligenceAvg.as_view(), name="avg-intelligence"),
    path('avg-strength/', views.HeroStrengthAvg.as_view(), name="avg-strength"),
    path('avg-speed/', views.HeroSpeedAvg.as_view(), name="avg-speed"),
    path('avg-durability/', views.HeroDurabilityAvg.as_view(), name="avg-durability"),
    path('avg-power/', views.HeroPowerAvg.as_view(), name="avg-power"),
    path('avg-combat/', views.HeroCombatAvg.as_view(), name="avg-combat"),
    path('swagger/', schema_view.with_ui("swagger",  cache_timeout=0), name="schema-swagger-ui"),

]

urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views_static.serve),
    ]
