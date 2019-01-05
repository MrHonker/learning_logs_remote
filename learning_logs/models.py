from django.db import models


# Create your models here.
class Topic(models.Model):
    """"用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    text = models.TextField()
    # 此处定义的属性在views里面会被函数调用，如果拼错会出现如下错误
    #Cannot resolve keyword 'date_added' into field. Choices are: data_added, id, text, topic, topic_id
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] +  "..."