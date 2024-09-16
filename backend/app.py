from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os
import re

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploaded_models'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return jsonify({"message": "Flask backend is running!"})

def parse_equation(equation):
    pattern = r"([-+]?\d*)x\^2\s*([-+]\s*\d+)x\s*([-+]\s*\d+)"
    match = re.search(pattern, equation.replace(" ", ""))
    if match:
        a = int(match.group(1)) if match.group(1) != "" and match.group(1) != "-" else -1 if match.group(1) == "-" else 1
        b = int(match.group(2).replace(" ", ""))
        c = int(match.group(3).replace(" ", ""))
        return a, b, c
    else:
        raise ValueError("The equation format is not recognized.")

@app.route('/api/upload-model', methods=['POST'])
def upload_model():
    if 'model' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['model']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        if filepath.endswith('.pkl'):
            model = pickle.load(open(filepath, 'rb'))
        elif filepath.endswith('.joblib'):
            model = joblib.load(filepath)
        else:
            return jsonify({'message': 'Unsupported file format'})
    except Exception as e:
        return jsonify({'message': f'Error loading model: {str(e)}'})

    return jsonify({'message': 'Model uploaded successfully!', 'model_filename': file.filename})

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    problem = data.get('problem')
    solution = data.get('solution')
    model_filename = data.get('model_filename')

    if not model_filename:
        return jsonify({'message': 'Model filename not provided'})

    model_path = os.path.join(app.config['UPLOAD_FOLDER'], model_filename)

    if not os.path.exists(model_path):
        return jsonify({'message': 'Model not found'})

    try:
        model = pickle.load(open(model_path, 'rb'))
    except Exception as e:
        return jsonify({'message': f'Error loading model: {str(e)}'})

    try:
        print(f"Problem: {problem}")  # Debugging
        print(f"Solution: {solution}")  # Debugging

        a, b, c = parse_equation(problem)
        coefficients = np.array([a, b, c]).reshape(1, -1)

        # Ensure solution is a list of floats
        solution = np.array(solution, dtype=float)
        
        prediction = model.predict(coefficients)
        
        # Ensure prediction is a list of floats
        prediction = np.array(prediction, dtype=float)

        # Calculate accuracy
        is_correct = np.allclose(prediction, solution, rtol=1e-2)
        accuracy = (100.0 if is_correct else 0.0)

        response = {
            'problem': problem,
            'solution': solution.tolist(),
            'message': f'Prediction accuracy: {accuracy:.2f}%',
            'accuracy': accuracy,
            'prediction': prediction.tolist()
        }
        print(f"Response: {response}")  # Debugging

        return jsonify(response)
    except Exception as e:
        return jsonify({'message': f'Error during evaluation: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
