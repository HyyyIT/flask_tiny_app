from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.utils import timezone
from .forms import CustomUserCreationForm
from .models import  CustomUser
from django.conf import settings


# Kiểm tra quyền admin
def is_admin(user):
    return user.is_superuser

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

# Đăng nhập
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('to_do_list')
            else:
                messages.error(request, "Tài khoản của bạn đã bị khóa.")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
    return render(request, 'login.html')

# Đăng xuất
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def to_do_list(request):
    return render(request, 'to_do_list.html')


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
    
    if request.method == "POST":
        user.is_active = not user.is_active
        user.save()
        
        # Thêm thông báo khi tài khoản bị khóa
        if not user.is_active:
            send_mail(
                'Tài khoản của bạn đã bị khóa',
                'Tài khoản của bạn đã bị khóa bởi quản trị viên.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            messages.warning(request, f"Tài khoản {user.username} đã bị khóa.")
        else:
            messages.success(request, f"Tài khoản {user.username} đã được mở khóa.")

        return redirect('admin_dashboard')

    return render(request, 'toggle-user-status.html', {'user': user})

# Reset mật khẩu người dùng
@login_required
@user_passes_test(is_admin)
def reset_user_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == "POST":
        new_password = request.POST.get("new_password", "newpassword123")
        user.set_password(new_password)
        user.save()
        
        # Gửi email thông báo mật khẩu mới
        send_mail(
            'Mật khẩu của bạn đã được đặt lại',
            f'Admin đã đặt lại mật khẩu của bạn. Mật khẩu mới là: {new_password}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )

        messages.success(request, f"Mật khẩu của {user.username} đã được đặt lại.")
        return redirect('admin_dashboard')

    return render(request, 'reset-user-password.html', {'user': user})