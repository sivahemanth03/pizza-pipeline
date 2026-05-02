from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(
        status='ok',
        service='service-b',
        message='Pizza tracking service is running!'
    )

@app.route('/api')
def api():
    return jsonify(
        message='Pizza Tracker API',
        orders=[
            {'id': 1, 'status': 'Baking', 'pizza': 'Margherita'},
            {'id': 2, 'status': 'Out for delivery', 'pizza': 'Pepperoni'}
        ]
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)