from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py，
对learning_logs 调用makemigrations ，以及让Django迁移项目。"""
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # 在Topic中添加字段owner ，它建立到模型User的外键关系。用户被删除
    # 时，所有与之相关联的主题也会被删除。
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    # 学到的有关某个主题的具体知识。
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # 返回模型的字符串表示。
        return f"{self.text[:50]}..."
