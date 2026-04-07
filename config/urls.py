from django.contrib import admin
from django.urls import path
from calculadora_poder.views import calcular_poder # Importamos tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/poder/<str:pokemon_name>/', calcular_poder, name='calcular_poder'),
]