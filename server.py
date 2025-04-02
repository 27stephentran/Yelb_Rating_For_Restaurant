import os
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


try:
    model = pickle.load(open('machinelearning_model.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

@app.route("/predict/", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")
    
    if not features:
        return jsonify({"error": "Dữ liệu không hợp lệ, 'features' không được cung cấp"}), 400
    
    try:
        features = [float(x) for x in features]
        prediction = model.predict([features])
        return jsonify({"predicted_class": prediction[0]})
    except Exception as e:
        return jsonify({"error": f"Xảy ra lỗi khi xử lý dữ liệu đầu vào: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
