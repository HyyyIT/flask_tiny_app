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
from .models import Task
from django.utils import timezone
from django.db import connection


# Trang chủ
def landing_page(request):
    return render(request, 'landing.html')

# Kiểm tra quyền admin
def is_admin(user):
    return user.is_superuser

# Đăng ký tài khoản
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Chưa lưu vào database ngay
            user.is_active = True  # Kích hoạt tài khoản
            user.save()  # Lưu tài khoản vào database
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
                return redirect('admin_dashboard' if user.is_superuser else 'to_do_list')
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
    tasks_list = Task.objects.filter(user=request.user).order_by('id')
    paginator = Paginator(tasks_list, 10)  # 10 công việc mỗi trang

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'to_do_list.html', {'tasks': tasks})

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
@login_required
def to_do_list(request):
    tasks_list = Task.objects.filter(user=request.user).order_by('id')
    paginator = Paginator(tasks_list, 10)  # 10 công việc mỗi trang

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'to_do_list.html', {
        'tasks': tasks,
        'paginator': paginator,
    })

# Xóa nhiều nhiệm vụ cùng lúc và reset ID
@login_required
def delete_multiple_tasks(request):
    if request.method == "POST":
        task_ids = request.POST.getlist("task_ids")
        Task.objects.filter(id__in=task_ids, user=request.user).delete()
        messages.success(request, "Các nhiệm vụ đã được xóa thành công.")
        reset_task_ids()
    return redirect('to_do_list')

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(user=request.user, title=title, completed=False, created_at=timezone.now(), updated_at=timezone.now())

            # Tính toán số trang mới nhất sau khi thêm công việc
            tasks_list = Task.objects.filter(user=request.user).order_by('id')
            paginator = Paginator(tasks_list, 10)  # 10 công việc mỗi trang
            last_page = paginator.num_pages  # Trang cuối cùng

            messages.success(request, "Công việc đã được thêm!")
            return redirect(f"{request.path}?page={last_page}")  # Điều hướng đến trang cuối cùng

    return redirect("to_do_list")


# Chỉnh sửa công việc với timestamp
@login_required 
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get("title", task.title)
        task.completed = "completed" in request.POST
        task.updated_at = timezone.now()
        task.save()
        messages.success(request, "Công việc đã được cập nhật!")
        return redirect("to_do_list")
    return render(request, "edit_task.html", {"task": task})

# Xóa công việc và reset ID
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, "Công việc đã bị xóa!")
    reset_task_ids()
    return redirect("to_do_list")

# Hàm reset lại ID sau khi xóa
def reset_task_ids():
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE sqlite_sequence SET seq = 0 WHERE name = 'to_do_list_task';
        """)
