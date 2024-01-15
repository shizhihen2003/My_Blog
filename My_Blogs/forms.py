from django import forms
from .models import Topic,Entry


# 在Diango中，创建表单的最简单方式是使用ModelForm
# 定义一个名为TopicForm 的类，它继承了forms.ModelForm
class TopicForm(forms.ModelForm):
    class Meta:
        # 根据模型Topic创建表单
        model = Topic
        # 其中只包含字段text
        fields = ['text']
        # 让Django不要为字段text生成标签
        labels = {'text': ' '}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # 给字段'text'指定了标签'Entry:'
        labels = {'text': ' '}

        # 小部件 （widget）是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets
        # ，可覆盖Django选择的默认小部件。通过让Django使用forms.Textarea
        # ，我们定制了字段'text'的输入小部件，将文本区域的宽度设置为80
        # 列，而不是默认的40列。这给用户提供了足够的空间来编写有意义的条目。
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
