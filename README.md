#  Poke Power API & Client

Este proyecto es una aplicación Web construida en arquitectura cliente-servidor que demuestra el consumo y la producción de Servicios Web (API RESTful). 

El backend actúa como un intermediario (Middleware): consume la PokeAPI pública, procesa los datos aplicando una lógica de negocio propia (cálculo del nivel de poder total) y produce un nuevo Web Service simplificado. El frontend es una interfaz de usuario limpia que consume este nuevo servicio.

## Tecnologías Utilizadas

* **Backend:** Python, Django, Django REST Framework.
* **Integraciones:** Librería `requests` para consumo HTTP externo y `django-cors-headers` para control de acceso.
* **Frontend:** HTML5, CSS3, JavaScript puro (Vanilla JS) y API Fetch.

## Requisitos Previos (Prerrequisitos)

Para ejecutar este proyecto en tu entorno local, asegúrate de tener instalado:
* **Python 3.8** o superior.
* **pip** (Gestor de paquetes de Python).
* **Git** (Para clonar el repositorio).

## Instalación y Ejecución paso a paso

Sigue estas instrucciones para levantar el proyecto en un entorno Linux/macOS:

### 1. Preparar el Servidor (Backend)

Abre tu terminal y ejecuta los siguientes comandos en orden:

```bash
# 1. Clona este repositorio (reemplaza con tu URL)
git clone [https://github.com/tu-usuario/poke-power-api.git](https://github.com/tu-usuario/poke-power-api.git)
cd poke-power-api

# 2. Crea y activa un entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instala las dependencias necesarias
pip install django djangorestframework requests django-cors-headers

# 4. Construye la base de datos de Django
python manage.py migrate

# 5. Enciende el servidor local
python manage.py runserver
