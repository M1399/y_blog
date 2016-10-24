# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
# Create your models here.

class Article(models.Model) :
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    
    #def get_absolute_url(self):
     #   path = reverse('detail', kwargs={'id':self.id})
      #  return "http://127.0.0.1:8000%s" % path
   

    #python3请使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

    def get_absolute_url(self):
	#解析detail视图函数对应的url
        return reverse('detail', kwargs={'id': self.pk})

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField()
 #def __unicode__(self):
#        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    
admin.site.register(User,UserAdmin)

class Category(models.Model): 
     class Meta: 
         app_label = 'blog' 
         verbose_name = '分类目录' 
         verbose_name_plural = '分类目录' 
 
 
     name = models.CharField(max_length=40) 
 
 
     def __str__(self): 
         return self.name 
#评论
class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    user_email = models.EmailField('评论者邮箱', max_length=255)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]
 
 
 
class Post(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
   # date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.pk})
 
    #python3请使用__str__
    def __str__(self) :
        return self.title

  #  class Meta:  #按时间下降排序
   #     ordering = ['-date_time']

