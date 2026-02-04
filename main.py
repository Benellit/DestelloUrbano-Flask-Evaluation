from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Simulación de Base de Datos
incidentes_db = []

# RUTA 1: Landing Page (La portada)
@app.route('/')
def index():
    # Asegúrate de que index.html esté en la carpeta templates (no en subcarpetas)
    return render_template('index.html')

# RUTA 2: El Mapa (La aplicación)
@app.route('/map')
def map_view():
    # Esta busca en templates/map/map.html
    return render_template('map/map.html')

# API: Guardar Puntos
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.get_json()
    
    if not data or 'lat' not in data or 'lng' not in data:
        return jsonify({'status': 'error', 'message': 'Datos inválidos'}), 400

    lat = data['lat']
    lng = data['lng']
    
    # Simulación de latencia
    time.sleep(1.0)
    
    nuevo_incidente = {
        'id': len(incidentes_db) + 1,
        'lat': lat,
        'lng': lng,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    incidentes_db.append(nuevo_incidente)
    
    return jsonify({
        'status': 'success', 
        'message': 'Ubicación registrada correctamente',
        'data': nuevo_incidente
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)