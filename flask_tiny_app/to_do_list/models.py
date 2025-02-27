from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    failed_login_attempts = models.IntegerField(default=0)

    # email = models.EmailField(unique=True)  # Thêm email vào model

    def __str__(self):
        return self.username 


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Tự động đặt khi tạo mới
    updated_at = models.DateTimeField(auto_now=True)  # Tự động cập nhật khi chỉnh sửa

    def __str__(self):
        return self.title

