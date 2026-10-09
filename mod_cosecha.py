from flask import Blueprint, request, jsonify

# 1. Crear el Blueprint para el módulo
cosecha_bp = Blueprint('cosecha', __name__)

# 2. Inicializar las listas para almacenar la información en memoria 
cosechas = []
ventas = []
@cosecha_bp.route('/cosechas', methods=['POST'])
def registrar_cosecha():
    datos = request.get_json()
    nueva_cosecha = {
        "id": len(cosechas) + 1,
        "lote_id": datos.get("lote_id"),
        "kilos_obtenidos": datos.get("kilos_obtenidos"),
        "fecha": datos.get("fecha")
    }
    cosechas.append(nueva_cosecha)
    return jsonify({"mensaje": "Cosecha registrada con éxito", "cosecha": nueva_cosecha}), 201

@cosecha_bp.route('/ventas', methods=['POST'])
def registrar_venta():
    datos = request.get_json()
    nueva_venta = {
        "id": len(ventas) + 1,
        "cosecha_id": datos.get("cosecha_id"),
        "cliente": datos.get("cliente"),
        "kilos_vendidos": datos.get("kilos_vendidos"),
        "total_cop": datos.get("total_cop")
    }
    ventas.append(nueva_venta)
    return jsonify({"mensaje": "Venta registrada con éxito", "venta": nueva_venta}), 201
