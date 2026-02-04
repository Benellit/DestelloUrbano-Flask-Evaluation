from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Simulación de Base de Datos
incidentes_db = []

@app.route('/')
def map_view():
    # CORRECCIÓN: Agregamos 'map/' antes del nombre del archivo
    # porque en tu carpeta templates lo tienes dentro de una subcarpeta "map"
    return render_template('map/map.html')

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    """
    Endpoint que recibe coordenadas y simula un guardado.
    Incluye un delay artificial para probar el estado 'Cargando...' en el frontend.
    """
    data = request.get_json()
    
    if not data or 'lat' not in data or 'lng' not in data:
        return jsonify({'status': 'error', 'message': 'Datos inválidos'}), 400

    lat = data['lat']
    lng = data['lng']
    
    # Simulamos latencia de red (1.5 segundos) para ver el spinner
    time.sleep(1.5)
    
    nuevo_incidente = {
        'id': len(incidentes_db) + 1,
        'lat': lat,
        'lng': lng,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    incidentes_db.append(nuevo_incidente)
    
    # print(f"✅ Punto guardado: {nuevo_incidente}") # Opcional: ver en consola
    
    return jsonify({
        'status': 'success', 
        'message': 'Ubicación registrada correctamente',
        'data': nuevo_incidente
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)