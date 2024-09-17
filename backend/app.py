# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from models.model_handler import load_model, save_model  # Import from models folder
from utils.error_handling import invalid_input_error, model_not_found_error, evaluation_error
from database.db_setup import save_model as db_save_model, save_performance  # Import from database folder

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

@app.route('/api/upload-model', methods=['POST'])
def upload_model():
    """Handle model file upload and save it to both disk and database."""
    if 'model' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['model']
    filename = file.filename

    # Save the model file to disk
    model_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    save_model(file, model_file_path)  # Save the model file to disk

    # Save model in the database
    model_id = db_save_model(filename, model_file_path)

    if model_id:
        return jsonify({'message': 'Model uploaded successfully', 'model_id': model_id})
    else:
        return jsonify({'message': 'Model upload failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
