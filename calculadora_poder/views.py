from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def calcular_poder(request, pokemon_name):
    # Aqui llamo a mi API externa
    url_pokeapi = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    respuesta_externa = requests.get(url_pokeapi)

    # En caso de que el nombre del pokemon este erroneo
    if respuesta_externa.status_code != 200:
        return Response({"error": "Pokémon no encontrado"}, status=404)

    # Extraigo la info recibida para poder usarla
    datos = respuesta_externa.json()

    # Proceso para sumar las stats del pokemon que queremos saber
    poder_total = 0
    for stat in datos['stats']:
        poder_total += stat['base_stat']

    # Json del bolsillo
    mi_respuesta = {
        "nombre": datos['name'].capitalize(),
        "tipo_principal": datos['types'][0]['type']['name'],
        "imagen": datos['sprites']['front_default'],
        "nivel_de_poder_total": poder_total,
        "mensaje": f"El nivel de poder de {datos['name'].capitalize()} es {poder_total}."
    }

    # Mostramos el web service
    return Response(mi_respuesta)