import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL của API mà bạn sẽ gọi
API_URL = os.environ.get("API_URL", "https://yelb-rating-for-restaurant.onrender.com/predict/")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        features = request.form.get("features")
        
        # In giá trị features ra để kiểm tra dữ liệu
        print(f"Received features: {features}")

        try:
            # Chuyển đổi dữ liệu từ chuỗi thành danh sách số thực
            features_list = list(map(float, features.split(",")))

            # Gửi yêu cầu POST đến API
            response = requests.post(API_URL, json={"features": features_list})

            # In ra status code và nội dung phản hồi để gỡ lỗi
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            # Kiểm tra nếu API trả về status 200 thì lấy dự đoán
            if response.status_code == 200:
                prediction = response.json().get("predicted_class")
            else:
                # In chi tiết lỗi nếu không phải mã 200
                prediction = f"Lỗi API: {response.status_code} - {response.text}"

        except Exception as e:
            # In chi tiết lỗi khi dữ liệu không hợp lệ
            prediction = f"Dữ liệu không hợp lệ: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway sẽ tự động cung cấp PORT
    app.run(host="0.0.0.0", port=port)
