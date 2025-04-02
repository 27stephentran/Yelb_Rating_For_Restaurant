# Sử dụng Python image
FROM python:3.9-slim

# Cài đặt thư viện cần thiết
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào Docker container
COPY . .

# Expose port 5000
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "client.py"]
