import os
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


model = pickle.load(open('machinelearning_model.pkl', 'rb'))

@app.route("/predict/", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")
    
    if features:
        prediction = model.predict([features]) 
        return jsonify({"predicted_class": prediction[0]})  
    return jsonify({"error": "Dữ liệu không hợp lệ"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
