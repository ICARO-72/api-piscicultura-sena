from flask import Blueprint, request, jsonify

lotes_bp = Blueprint('lotes', __name__)

lotes = []
alimentacion = []

@lotes_bp.route('/', methods=['POST'])
def registrar_lote():
    datos = request.get_json()
    nuevo_lote = {
        "id": len(lotes) + 1,
        "especie": datos.get("especie"),
        "cantidad_inicial": datos.get("cantidad_inicial"),
        "estanque_id": datos.get("estanque_id"),
        "estado": "En Crianza"
    }
    lotes.append(nuevo_lote)
    return jsonify({"mensaje": "Lote registrado exitosamente", "lote": nuevo_lote}), 201

@lotes_bp.route('/', methods=['GET'])
def listar_lotes():
    return jsonify(lotes), 200

@lotes_bp.route('/alimentacion', methods=['POST'])
def registrar_alimentacion():
    datos = request.get_json()
    registro = {
        "id": len(alimentacion) + 1,
        "lote_id": datos.get("lote_id"),
        "cantidad_kg": datos.get("cantidad_kg"),
        "tipo_alimento": datos.get("tipo_alimento")
    }
    alimentacion.append(registro)
    return jsonify({"mensaje": "Registro de alimentación guardado", "datos": registro}), 201
