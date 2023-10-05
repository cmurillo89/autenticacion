from django.urls import path, include
from .views import inicio, peliculas, salir

urlpatterns = [
    path('', inicio, name="inicio"),
    path('peliculas/', peliculas, name="peliculas"),
    path('salir/', salir, name="salir"),
]