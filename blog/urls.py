# blog/urls.py
from django.urls import path
from .views import post_list, post_detail, create_post, edit_post, login_view, signup_view, logout_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/add/', create_post, name='create_post'),
    path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('login/', login_view, name='login'),  # URL for login
    path('signup/', signup_view, name='signup'),  # URL for signup
    path('logout/', logout_view, name='logout'),
    path('login/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('login/password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('username_password_reset/', views.username_password_reset, name='username_password_reset'),
    # path('password_reset_confirm/<int:user_id>/', views.password_reset_confirm, name='password_reset_confirm'),
]
