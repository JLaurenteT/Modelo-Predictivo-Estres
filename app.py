from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar modelo entrenado
model = joblib.load('modelo_estres.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    try:
        data = request.get_json()

        # Crear DataFrame con las columnas en el MISMO orden que el entrenamiento
        columnas = ['PUNTUACION DEL SUENO', 'PUNTOS DE ACTIVIDAD FISICA', 'HRV']
        valores = [[
            float(data.get('PUNTUACION DEL SUENO', 0)),
            float(data.get('PUNTOS DE ACTIVIDAD FISICA', 0)),
            float(data.get('HRV', 0))
        ]]

        df = pd.DataFrame(valores, columns=columnas)

        pred = model.predict(df)[0]
        return jsonify({'categoria_estres': pred})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto de Render o 5000 por defecto
    app.run(host='0.0.0.0', port=port)