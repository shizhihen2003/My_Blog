# 定义my_blogs的URL模式。
from django.urls import path
from . import views

app_name = 'My_Blogs'
urlpatterns = [
    # 主页
    # 实际的URL模式是对函数path() 的调用，这个函数接受三个实参（见❺）。第一个
    # 是一个字符串，帮助Django正确地路由（route）请求。收到请求的URL后，Django
    # 力图将请求路由给一个视图。为此，它搜索所有的URL模式，找到与当前请求匹配的
    # 那个。Django忽略项目的基础URL（http://localhost:8000/），因此空字符串（'' ）与基础URL匹配。其他URL都与这个模式不匹配。如果请求的URL与任何既有的URL
    # 模式都不匹配，Django将返回一个错误页面。
    # path() 的第二个实参（见❻）指定了要调用view.py中的哪个函数。请求的URL与
    # 前述正则表达式匹配时，Django将调用view.py中的函数index() （这个视图函数
    # 将在下一节编写）。第三个实参将这个URL模式的名称指定为index ，让我们能够
    # 在代码的其他地方引用它。每当需要提供到这个主页的链接时，都将使用这个名
    # 称，而不编写URL。
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topic/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('contact us', views.contact_us, name='contact us'),
]