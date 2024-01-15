from django.shortcuts import render, redirect
# 函数render() ，它根据视图提供的数据渲染响应。
# Create your views here.
from django.contrib.auth.decorators import login_required
# 导入与所需数据相关联的模型
from.models import Topic, Entry
from django.http import Http404
from .forms import TopicForm, EntryForm


# 为主页编写视图
def index(request):
    # 博客主页
    return render(request, 'My_Blogs/index.html')

# 除request 对象外，第一个还包含另一个形参的视图函数。这个函数接受
# 表达式/<int:topic_id>/ 捕获的值，并将其存储到topic_id 中


@login_required
def topics(request):
    # 显示主页

    # 查询数据库——请求提供Topic对象，并根据属性date_added 进行排序。返回的查询集被
    # 存储在topics 中。
    # topics = Topic.objects.order_by('date_added')

    # 用户登录后，request对象将有一个user属性，其中存储了有关该用户的
    # 信息。查询Topic.objects.filter(owner=request.user)让
    # Django只从数据库中获取owner属性为当前用户的Topic对象。
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    # 定义一个将发送给模板的上下文。上下文是一个字典，其中的键是将
    # 在模板中用来访问数据的名称，而值是要发送给模板的数据。这里只有一个键
    # 值对，包含一组将在页面中显示的主题。
    context = {'topics': topics}

    # 创建使用数据的页面时，除了对象request
    # 和模板的路径外，还将变量context传递给render()
    return render(request, 'My_Blogs/topics.html', context)


@login_required
# def topic(request, topic_id):
#     # 显示单个主题及其所有的条目。
#     topic = Topic.objects.get(id=topic_id)
#     if topic.owner != request.user:
#         raise Http404
#     # 获取与该主题相关联的条目，并根据date_added进行排序：date_added
#     # 前面的减号指定按降序排列，即先显示最近的条目。
#     entries = topic.entry_set.order_by('-date_added')
#
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'My_Blogs/topic.html', context)
def topic(request):
    return render(request, 'My_Blogs/topic.html')


@login_required
def new_topic(request):
    """添加新主题。"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        # 创建一个TopicForm实例，将其赋给变量form ，再通
        # 过上下文字典将这个表单发送给模板由于实例化TopicForm时
        # 没有指定任何实参，Django将创建一个空表单，供用户填写。
        form = TopicForm()

    else:
        # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():    #法is_valid() 核实用户填写了所有必不可少的字段（表单字段默认都是必不
                                # 可少的），且输入的数据与要求的字段类型一致

            # 首先调用form.save()并传递实参commit = False，因为要先
            # 修改新主题，再将其保存到数据库。
            new_topic = form.save(commit=False)

            # 将新主题的owner属性设置为当前用户
            new_topic.owner = request.user

            new_topic.save()
        # form.save()
            return redirect('My_Blogs:topics')
    # 显示空表单或指出表单数据无效。
    context = {'form': form}
    return render(request, 'My_Blogs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定主题中添加新条目。"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据：创建一个空表单。
        form = EntryForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 传递实参commit = False ，让Django创建一个
            # 新的条目对象，并将其赋给new_entry ，但不保存到数据库中
            new_entry = form.save(commit=False)

            # 将new_entry的属性topic设置为在这个函数开头从数据库中获取的主题
            # ，再调用save()且不指定任何实参。这将把条目保存到数据
            # 库，并将其与正确的主题相关联
            new_entry.topic = topic
            new_entry.save()

            return redirect('My_Blogs:topic', topic_id=topic_id)
    # 显示空表单或指出表单数据无效。
    context = {'topic': topic, 'form': form}
    return render(request, 'My_Blogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目。"""

    # 获取用户要修改的条目对象以及与其相关联的主题
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据：对数据进行处理。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('My_Blogs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'My_Blogs/edit_entry.html', context)


def contact_us(request):
    return render(request, 'My_Blogs/contact us.html')