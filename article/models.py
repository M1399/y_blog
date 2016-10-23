# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
   

    #python3请使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']


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
 
class Postjh(models.Model):
    class Meta:
        app_label = 'blog'
        verbose_name = '文章'
        verbose_name_plural = '文章'

    # 作者
   # author = models.ForeignKey(User)
    # 标题
    title = models.CharField(max_length=200)
    # 正文
    text = models.TextField()
    # 标签
    #tags = models.ManyToManyField(Tag)
    # 分类目录
    #category = models.ForeignKey(Category)
    # 点击量
    #click = models.IntegerField(default=0)
    # 创建时间
    #created_date = models.DateTimeField(default=timezone.now)
    # 发布时间
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
 
 
class Post(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
   # date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
 
    #python3请使用__str__
    def __str__(self) :
        return self.title

  #  class Meta:  #按时间下降排序
   #     ordering = ['-date_time']

