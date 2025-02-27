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

# # Quên mật khẩu
# def password_reset(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             new_password = form.cleaned_data['new_password']
#             user.set_password(new_password)
#             user.save()
#             send_mail(
#                 'Đặt lại mật khẩu thành công',
#                 'Mật khẩu của bạn đã được đặt lại thành công.',
#                 settings.DEFAULT_FROM_EMAIL,
#                 [user.email],
#             )
#             messages.success(request, "Mật khẩu đã được cập nhật. Hãy đăng nhập lại.")
#             return redirect('login')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'password_reset.html', {'form': form})

