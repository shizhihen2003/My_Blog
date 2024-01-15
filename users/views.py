# 导入函数render() 和redirect() ，然后导入函数login()
# ，以便在用户正确填写了注册信息时让其自动登录。我们还导入了默
# 认表单UserCreationForm 。
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """注册新用户。"""
    if request.method != 'POST':
        # 显示空的注册表单。
        form = UserCreationForm()
    else:
        # 处理填写好的表单。
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # 方法save()返回新创建的用户对象，将它赋给了new_user 。
            new_user = form.save()

            # 让用户自动登录，再重定向到主页。
        # 保存用户的信息后，调用函数login()并传入对象request
        # 和new_user ，为用户创建有效的会话，从而让其自动登录
            login(request, new_user)

            return redirect('My_Blogs:index')
    # 显示空表单或指出表单无效。
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def user_login(request):
    # 检查请求是否为POST类型，这通常意味着表单已被提交
    if request.method == 'POST':
        # 从POST请求中获取用户名和密码
        username = request.POST['username']
        password = request.POST['password']

        # 使用Django的authenticate函数验证用户名和密码
        user = authenticate(request, username=username, password=password)

        # 如果认证成功，user将不为None
        if user is not None:
            # 使用Django的login函数登录用户，创建用户会话
            login(request, user)
            # 登录成功后重定向到指定页面，这里是'My_Blogs:index'
            return redirect('My_Blogs:index')
        else:
            # 如果认证失败，向用户显示错误消息
            messages.error(request, 'Invalid username or password')
            # 重新渲染登录页面，显示错误信息
            return render(request, 'registration/login.html')
    else:
        # 如果请求不是POST（如GET请求），显示登录表单
        return render(request, 'registration/login.html')
