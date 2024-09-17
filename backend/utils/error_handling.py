from flask import jsonify

def error_response(message):
    return jsonify({
        "error": message
    })

def invalid_input_error():
    return error_response("Invalid input or unsolvable problem")

def model_not_found_error():
    return error_response("Model not found")

def model_loading_error(error_msg):
    return error_response(f"Error loading model: {error_msg}")

def evaluation_error(error_msg):
    return error_response(f"Error during evaluation: {error_msg}")
