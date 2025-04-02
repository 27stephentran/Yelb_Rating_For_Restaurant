import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "https://yelb-rating-for-restaurant.onrender.com/predict/")

@app.route("/", methods=["GET", "POST"])
def index():
    print(API_URL)
    prediction = None
    if request.method == "POST":
        features = request.form.get("features")
        
        print(f"Received features: {features}")

        try:
            features_list = list(map(float, features.split(",")))

            response = requests.post(API_URL, json={"features": features_list})

            print(f"Response Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code == 200:
                prediction = response.json().get("predicted_class")
            else:
                prediction = f"Lỗi API: {response.status_code} - {response.text}"

        except Exception as e:
            prediction = f"Dữ liệu không hợp lệ: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
