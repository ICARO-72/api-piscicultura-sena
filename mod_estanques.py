from flask import Blueprint, request, jsonify
# 1. Crear el Blueprint para el módulo
estanques_bp = Blueprint('estanques', __name__)
# 2. Inicializar las listas para almacenar la información en memoria
estanques = []
lecturas_agua = []
@estanques_bp.route('/', methods=['POST'])
def registrar_estanque():
    datos = request.get_json()
    nuevo_estanque = {
        "id": len(estanques) + 1,
        "nombre": datos.get("nombre"),
        "dimension_m2": datos.get("dimension_m2"),
        "estado": datos.get("estado", "Activo")
    }
    estanques.append(nuevo_estanque)
    return jsonify({"mensaje": "Estanque registrado exitosamente", "estanque": nuevo_estanque}), 201

@estanques_bp.route('/', methods=['GET'])
def listar_estanques():
    return jsonify(estanques), 200

@estanques_bp.route('/lecturas', methods=['POST'])
def registrar_lectura_agua():
    datos = request.get_json()
    nueva_lectura = {
        "id": len(lecturas_agua) + 1,
        "estanque_id": datos.get("estanque_id"),
        "ph": datos.get("ph"),
        "oxigeno_mg_l": datos.get("oxigeno_mg_l"),
        "fecha": datos.get("fecha")
    }
    lecturas_agua.append(nueva_lectura)
    return jsonify({"mensaje": "Lectura de agua registrada", "lectura": nueva_lectura}), 201

@estanques_bp.route('/api/estanques/lecturas', methods=['GET'])
def consultar_lecturas():
    return jsonify(lecturas_agua), 200