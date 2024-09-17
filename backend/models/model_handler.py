import os
import pickle
import joblib
from flask import jsonify

UPLOAD_FOLDER = 'uploaded_models'

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def load_model(filename):
    try:
        if filename.endswith('.pkl'):
            model = pickle.load(open(os.path.join(UPLOAD_FOLDER, filename), 'rb'))
        elif filename.endswith('.joblib'):
            model = joblib.load(os.path.join(UPLOAD_FOLDER, filename))
        else:
            return jsonify({'message': 'Unsupported file format'})
        return model
    except Exception as e:
        return jsonify({'message': f'Error loading model: {str(e)}'})

def save_model(file):
    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({'message': 'Model uploaded successfully!', 'model_filename': file.filename})
