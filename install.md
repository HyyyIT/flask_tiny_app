# Cài đặt môi trường ảo
python -m venv venv
# venv\Scripts\activate  # Trên Windows (chạy riêng nếu dùng Windows)

echo "Môi trường ảo đã được kích hoạt."

# Cài đặt các gói cần thiết
pip install --upgrade pip
pip install -r requirements.txt

# Chạy migrate để thiết lập database
python manage.py makemigrations
python manage.py migrate
echo "Database đã được migrate thành công."

# Tạo tài khoản admin (tùy chọn)
read -p "Bạn có muốn tạo tài khoản admin không? (y/n): " create_admin
if [ "$create_admin" == "y" ]; then
    python manage.py createsuperuser
fi

echo "Cấu hình hoàn tất! Hãy chạy python manage.py runserver để khởi động dự án."
