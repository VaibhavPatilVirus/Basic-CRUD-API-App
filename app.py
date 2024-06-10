from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    try:
        return jsonify({"error":"Not a valid API endpoint."}), 405
    except Exception as e:
        return jsonify({"error":"Internal server error."}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')