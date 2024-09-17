# utils/error_handling.py
from flask import jsonify

def invalid_input_error():
    """Return an error response for invalid input format."""
    return jsonify({'message': 'Invalid input format'}), 400

def model_not_found_error():
    """Return an error response for model not found."""
    return jsonify({'message': 'Model not found'}), 404

def model_loading_error():
    """Return an error response for issues loading a model."""
    return jsonify({'message': 'Error loading model'}), 500

def evaluation_error(error_message):
    """Return an error response for evaluation errors with a custom message."""
    return jsonify({'message': f'Evaluation error: {error_message}'}), 500
