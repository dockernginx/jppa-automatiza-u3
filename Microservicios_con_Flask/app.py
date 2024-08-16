from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_products():
    return jsonify({"success":"Welcome"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
