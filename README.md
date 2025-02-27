# flask-tiny-app-
a. Thông tin cá nhân (Họ tên, mã sinh viên)
Sinh viên 1:
Họ tên: Đỗ Tấn Đạt
Mã sinh viên: 22648601 
Sinh viên 2: Nguyễn Đăng Tuấn Huy
Mã sinh viên: 22658341

b. Mô tả project (mô tả ý tưởng mà bạn dự định làm)
TaskFlow - Ứng dụng Quản lý Công việc Hiệu Quả
Mô tả tổng quan:
TaskFlow giúp cá nhân và nhóm làm việc dễ dàng lập kế hoạch, theo dõi và hoàn thành nhiệm vụ. Ứng dụng tích hợp hệ thống thông báo thông minh và hỗ trợ làm việc nhóm, giúp tăng hiệu suất làm việc và tối ưu hóa quy trình quản lý công việc.

Các chức năng chính:
1. Hệ thống đăng nhập & đăng ký
Đăng ký tài khoản bằng email và mật khẩu.
Hỗ trợ xác thực qua email (tùy chọn).
Đăng nhập bảo mật với mật khẩu mã hóa.
Chức năng "Quên mật khẩu" để đặt lại mật khẩu qua email.
2. Trang quản trị (Admin Dashboard)
Quản lý người dùng: Danh sách tất cả tài khoản người dùng.
Khóa/Mở khóa tài khoản: Người dùng bị khóa sẽ không thể đăng nhập và nhận được thông báo “Tài khoản của bạn đã bị khóa.”
Reset mật khẩu: Admin có thể đặt lại mật khẩu cho người dùng.
Tìm kiếm & lọc người dùng: Hỗ trợ tìm kiếm theo email, trạng thái tài khoản.
3. Quản lý bài viết (posts) hoặc nhiệm vụ (tasks)
Người dùng có thể tạo, chỉnh sửa, xóa bài viết hoặc nhiệm vụ.
Xóa nhiều bài viết/nhiệm vụ cùng lúc để tiết kiệm thời gian.
Gắn thẻ (tags) cho nhiệm vụ để phân loại dễ dàng.
Bộ lọc nâng cao giúp tìm kiếm nhiệm vụ theo trạng thái (đang thực hiện, đã hoàn thành, quá hạn).
4. Phân trang (Pagination)
Mặc định hiển thị 10 bài viết/nhiệm vụ mỗi trang.
Người dùng có thể điều hướng giữa các trang để xem thêm nội dung.
Hỗ trợ tùy chỉnh số lượng nhiệm vụ hiển thị trên mỗi trang.
5. Hệ thống thông báo (MỚI)
Thông báo thời gian thực: Hiển thị thông báo khi có nhiệm vụ sắp đến hạn, khi có thay đổi trong nhóm hoặc khi tài khoản bị khóa.
Email nhắc nhở: Gửi email thông báo nhiệm vụ sắp đến hạn hoặc chưa hoàn thành.
Thông báo đẩy (push notification): Nếu người dùng sử dụng ứng dụng trên di động, hệ thống có thể gửi thông báo đẩy.
Tùy chỉnh thông báo: Người dùng có thể bật/tắt thông báo cho từng loại sự kiện.
6. Hỗ trợ nhóm (Teamwork) (MỚI)
Tạo nhóm làm việc: Người dùng có thể tạo nhóm và mời thành viên vào nhóm.
Phân quyền trong nhóm:
Chủ nhóm (Owner): Quản lý nhóm, thêm/xóa thành viên, phân quyền.
Quản lý (Manager): Quản lý nhiệm vụ trong nhóm, giao việc cho thành viên khác.
Thành viên (Member): Thực hiện nhiệm vụ được giao.
Giao nhiệm vụ nhóm: Cho phép giao nhiệm vụ cho từng thành viên hoặc cả nhóm.
Theo dõi tiến độ: Hiển thị tiến độ hoàn thành của từng nhiệm vụ và của cả nhóm.
Bình luận & trao đổi: Cho phép thành viên nhóm bình luận trên từng nhiệm vụ để trao đổi công việc.
c. Hướng dẫn cài đặt, chạy 
d. Link project đã triển khai của bạn