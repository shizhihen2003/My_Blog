# 定义my_blogs的URL模式。
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL。
    # 这个URL中的单词users让Django在users/urls.py中查找，而单词
    # login让它将请求发送给Django的默认视图login
    path('', include('django.contrib.auth.urls')),
    path('Sign_Up/', views.register, name='register'),
    path('Log_In/', views.user_login, name='login'),
    # 在 urls.py 中，你已经包含了 django.contrib.auth.urls，这可能会导致与你自定义的登录视图冲突。你应该确保使用自定义登录视图的 URL 不与 Django 内置的登录视图 URL 相冲突。如果你的自定义登录视图路径是 'login/'，则可能与 Django 默认的登录视图冲突。
]