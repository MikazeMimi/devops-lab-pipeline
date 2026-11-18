from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running", "service": "devops-lab-api"})

@app.route("/health")
def health():
    return jsonify({"healthy": False}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
