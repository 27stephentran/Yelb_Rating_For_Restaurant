# Sử dụng image chính thức của Python 3.10
FROM python:3.10

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép requirements.txt vào container
COPY requirements.txt .

# Cập nhật pip lên phiên bản mới nhất
RUN pip install --upgrade pip

# Cài đặt các thư viện từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào Docker container
COPY . .

# Chạy ứng dụng
CMD ["python", "app.py"]  # Hoặc tên file Python chính của bạn
