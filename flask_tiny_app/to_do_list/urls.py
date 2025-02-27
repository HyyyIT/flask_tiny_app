from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('to-do-list/', views.to_do_list, name='to_do_list'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('toggle-user-status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('reset-user-password/<int:user_id>/', views.reset_user_password, name='reset_user_password'),
]


