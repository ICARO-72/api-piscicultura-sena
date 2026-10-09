from flask import Flask, jsonify
# 1. Importar los Blueprints de cada módulo
from mod_estanques import estanques_bp
from mod_lotes import lotes_bp
from mod_cosecha import cosecha_bp

# 2. Inicializar la aplicación Flask
app = Flask(__name__)

# 3. Registrar los módulos (Blueprints) con su prefijo de URL
app.register_blueprint(estanques_bp, url_prefix='/api/v1/estanques')
app.register_blueprint(lotes_bp, url_prefix='/api/v1/lotes')
app.register_blueprint(cosecha_bp, url_prefix='/api/v1/cosecha')

# Ruta raíz para verificar la salud de la API
@app.route('/', methods=['GET'])
def inicio():
    return jsonify({
        "mensaje": "¡Bienvenido a la API de Gestión Acuícola SENA!",
        "version": "1.0.0",
        "modulos_disponibles": [
            "/api/v1/estanques",
            "/api/v1/lotes",
            "/api/v1/cosecha"
        ]
    }), 200

# 4. Punto de entrada principal para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)