import os
import pickle
import joblib
from flask import jsonify

UPLOAD_FOLDER = 'uploaded_models'

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def load_model(filename):
    """Load a model from the given filename."""
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if filename.endswith('.pkl'):
            with open(file_path, 'rb') as file:
                model = pickle.load(file)
        elif filename.endswith('.joblib'):
            model = joblib.load(file_path)
        else:
            return jsonify({'message': 'Unsupported file format'}), 400
        return model
    except Exception as e:
        return jsonify({'message': f'Error loading model: {str(e)}'}), 500

def save_model(file, model_file_path=None):
    """Save the uploaded model file to the specified path or default upload folder."""
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    try:
        if model_file_path:
            filepath = model_file_path
        else:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(filepath)
        return jsonify({'message': 'Model uploaded successfully!', 'model_filename': file.filename}), 200
    except Exception as e:
        return jsonify({'message': f'Error saving model: {str(e)}'}), 500
