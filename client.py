import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "https://yelb-rating-for-restaurant.onrender.com/predict/")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        features = request.form.get("features")
        try:
            features_list = list(map(float, features.split(",")))
            response = requests.post(API_URL, json={"features": features_list})

            if response.status_code == 200:
                prediction = response.json().get("predicted_class")
            else:
                prediction = "Lỗi API"
        except Exception:
            prediction = "Dữ liệu không hợp lệ"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)  
