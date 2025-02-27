TaskFlow - Ứng dụng Quản lý Công Việc Hiệu Quả 🚀
📌 Giới thiệu
TaskFlow là một ứng dụng quản lý công việc giúp cá nhân và nhóm làm việc dễ dàng lập kế hoạch, theo dõi và hoàn thành nhiệm vụ. 

👨‍💻 Nhóm phát triển
📌 Đỗ Tấn Đạt - Mã sinh viên: 22648601
📌 Nguyễn Đăng Tuấn Huy - Mã sinh viên: 22658341

🌟 Chức năng chính
🔐 Hệ thống đăng nhập & đăng ký
✔️ Đăng ký tài khoản bằng email và mật khẩu.
✔️ Xác thực qua email (tùy chọn).
✔️ Đăng nhập bảo mật với mật khẩu mã hóa.
✔️ Chức năng "Quên mật khẩu" để đặt lại mật khẩu qua email.

🛠️ Trang quản trị (Admin Dashboard)
✔️ Quản lý danh sách tài khoản người dùng.
✔️ Khóa/Mở khóa tài khoản: Người dùng bị khóa sẽ không thể đăng nhập và nhận được thông báo.
✔️ Reset mật khẩu: Admin có thể đặt lại mật khẩu cho người dùng.
✔️ Tìm kiếm & lọc người dùng theo email, trạng thái tài khoản.

📌 Quản lý nhiệm vụ (Tasks)
✔️ Tạo, chỉnh sửa, xóa nhiệm vụ.
✔️ Xóa nhiều nhiệm vụ cùng lúc để tiết kiệm thời gian.
✔️ Gắn thẻ (tags) để phân loại nhiệm vụ.
✔️ Bộ lọc nâng cao giúp tìm kiếm nhiệm vụ theo trạng thái.

📊 Phân trang (Pagination)
✔️ Mặc định hiển thị 10 nhiệm vụ mỗi trang.
✔️ Hỗ trợ chuyển trang nhanh với giao diện trực quan.
✔️ Tùy chỉnh số lượng nhiệm vụ hiển thị trên mỗi trang.

🛠️ Hướng dẫn cài đặt & chạy
Yêu cầu hệ thống
Python 3.x
Django
Thư viện hỗ trợ: django-crispy-forms, crispy-bootstrap5

Bước 1: Clone repository
mkdir TaskFlow
cd TaskFlow
git clone https://github.com/HyyyIT/taskflow.git

Bước 2: Tạo môi trường ảo & cài đặt dependencies
python -m venv venv
source venv/bin/activate  # Trên macOS/Linux
venv\Scripts\activate     # Trên Windows
pip install -r requirements.txt

Bước 3: Chạy ứng dụng
python manage.py runserver

Ứng dụng sẽ chạy tại: http://127.0.0.1:8000/

🚀 Công nghệ sử dụng
Backend: Django
Frontend: HTML, CSS (Bootstrap)
Database: SQLite
📞 Liên hệ & Hỗ trợ
📧 Email:

huy298445@gmail.com
dodat2004py@gmail.com
🐙 GitHub:

DanieSalin
HyyyIT
💼 LinkedIn:

Đỗ Tấn Đạt
Nguyễn Đăng Tuấn Huy
⭐ Hãy nhấn Star 🌟 repo nếu bạn thấy dự án hữu ích!