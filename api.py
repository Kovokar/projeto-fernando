# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importando o CORS


app = Flask(__name__)
CORS(app)


# Rota GET
@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "GET request received"}), 200

# Rota POST
@app.route('/temperatura-automatica', methods=['POST'])
def post_data():
    data = request.json
    if not data or 'temperatura' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    if 'ie_manual' in data:
        return jsonify({"error: Impossivel alterar"})

    temp_ideal = round(calcular_temperatura_ideal(data['umidade']))
    return jsonify({"message": f"Temperatura alterada para: {temp_ideal}C"}), 200


@app.route('/temperatura-manual', methods=['POST'])
def manual():
    data = request.json
    if not data or 'temperatura' not in data:
        return jsonify({"message": "Bad request"}), 400
    
    # Se o valor de 'ie_manual' for fornecido, o backend pode processar ou ignorar
    if 'ie_manual' in data:
        return jsonify({"message": f"Temperatura manual ajustada para: {data['temperatura']}°C"}), 200
    
    return jsonify({"message": f"Temperatura ajustada para: {data['temperatura']} C"}), 200

def calcular_temperatura_ideal(umidade_relativa):
    calc = ((umidade_relativa - 50) / 10)
    if calc < 0:
        calc *= -1
    temperatura_ideal = 22 - calc
    return temperatura_ideal



if __name__ == '__main__':
    app.run(debug=True)