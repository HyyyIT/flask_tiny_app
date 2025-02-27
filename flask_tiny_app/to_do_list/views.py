from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.utils import timezone
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.conf import settings



def landing_page(request):
    return render(request, 'landing.html')  # Trang landing page khi vào trang chủ
# Đăng ký tài khoản
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('to_do_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, f"Chào mừng {user.username}! Bạn đang đăng nhập với quyền: {'Admin' if user.is_superuser else 'User'}")
                return redirect('admin_dashboard' if user.is_superuser else 'task_list')
            else:
                messages.error(request, "Tài khoản của bạn đã bị khóa.")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
    return render(request, 'login.html')


# Đăng xuất
def logout(request):
    auth_logout(request)
    return redirect('login')
# Kiểm tra quyền admin
def is_admin(user):
    return user.is_superuser

# Trang quản trị Admin
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = CustomUser.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

# Khóa/Mở khóa tài khoản người dùng
@login_required
@user_passes_test(is_admin)
def toggle_user_status(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, "Trạng thái tài khoản đã được cập nhật.")
    return redirect('admin_dashboard')

# Reset mật khẩu người dùng
@login_required
@user_passes_test(is_admin)
def reset_user_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    new_password = 'NewPassword123'  # Có thể thay thế bằng cách gửi email đặt lại mật khẩu
    user.set_password(new_password)
    user.save()
    messages.success(request, f"Mật khẩu của {user.username} đã được đặt lại.")
    return redirect('admin_dashboard')

