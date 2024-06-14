from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    response = {
        "message": "Data received",
        "temperature": temperature,
        "humidity": humidity
    }
    return jsonify(response)

@app.route('/', methods=['GET'])
def index():
    return "Send POST requests to /data endpoint"

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)