from django.db import models

# Create your models here.

class BookInfo(models.Model):
    '''图书模型类'''
    #图书名称
    book_title=models.CharField(max_length=20)
    #图书日期
    book_date=models.DateField()

    def __str__(self):
        return self.book_title

class People(models.Model):
    '''人物模型类'''
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    #设置外键
    #在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    #不然会报错：TypeError:__init__() missing 1 required positional argument :'on_delete'
    book_people=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
