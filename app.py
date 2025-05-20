from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        "message": "Hello, World!",
        "status": "success",
        "service": "Docker Assignment REST API"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to make it accessible outside the container
    app.run(host='0.0.0.0', port=8080, debug=False)
