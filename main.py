from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': '¡Hola desde el servidor local!',
        'status': 'success'
    })

@app.route('/test')
def test():
    return jsonify({
        'message': 'Ruta de prueba funcionando',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
