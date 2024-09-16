from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with React

# Example route to test if Flask is working
@app.route('/')
def index():
    return jsonify({"message": "Flask backend is running!"})

# Endpoint for receiving message from frontend
@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()  # Get JSON data from POST request
    message = data.get('message', '')  # Extract 'message' from JSON data

    print(f"Received message from frontend: {message}")

    # Example response back to frontend
    response = {'message': f'Backend received: {message}'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
