Destello Urbano / Enlace a la app en vivo https://benellit.pythonanywhere.com/ 

Destello Urbano es una plataforma web de monitoreo ciudadano que permite visualizar zonas seguras y reportar incidentes en tiempo real sobre un mapa interactivo nocturno. Diseñado para mejorar la seguridad en la movilidad urbana repartidores, peatones u otros mediante inteligencia colectiva.

Sigue estos pasos para levantar el entorno localmente:

1. Clonar el repositorio

git clone https://github.com/Benellit/DestelloUrbano-Flask-Evaluation.git


2. Configurar el entorno virtual (Recomendado)

# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Instalar dependencias

pip install flask 


4. Ejecutar la aplicación

python main.py


Visita http://127.0.0.1:5000 en tu navegador.


Stack:

Backend: Python 3.x, Flask (Microframework).

Frontend: HTML5, JavaScript (ES6).

Mapas: Leaflet.js con teselas de CartoDB Voyager.

Estilos: Tailwind CSS vía CDN.

APIs: OpenStreetMap Nominatim para la Geolocalización Inversa.

Iconografía: Lucide Icons.


Justificación de Diseño y UX

El diseño se centra en la sensación de seguridad visual especialmente en entornos nocturnos:

El mapa tiene un tono con propósito, No utilizamos mapas negros que dificultan la visualización de rutas ni blancos que deslumbran. Implementamos un filtro CSS con (brightness: 90%, sepia: 10%) sobre mapas claros para lograr un tono }legible y no tan cansado para la vista.


Ámbar (#f59e0b): Usado para acciones principales y alertas. Es el color que el ojo humano detecta más rápido en la oscuridad.

Azul Profundo (#1e3a8a): Transmite autoridad seguridad y calma .

Botones con áreas táctiles ampliadas (44px) para uso fácil en móviles.

Feedback: Las acciones de guardar se confirman con una animación, cambio de icono y notificaciones (Toasts).


Créditos:

Este código fue co-creado con Gemini Canvas de Google.

Prompt Principal: "Actúa como un Senior Frontend Developer. Crea una Landing Page para 'Destello Urbano' con un mapa urbano estilizado en 'Dark Mode', psicología de color azul profundo/ámbar y componentes flotantes para reportes de seguridad."

Iteración de Mapa: Desarrollo de lógica en Leaflet para marcadores temporales, estados de carga y geolocalización inversa para tener datos en coordenada y nombre.
