# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
<<<<<<< HEAD
from django.core.urlresolvers import reverse
=======
>>>>>>> 9ad492ca599a5059a8186f2e4ffabf56a851920c

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    
<<<<<<< HEAD
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
   

    #python3请使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']


=======
    #python3请使用__str__
    def __str__(self) :
        return self.title
    class Meta:  #按时间下降排序
        ordering = ['-date_time']

>>>>>>> 9ad492ca599a5059a8186f2e4ffabf56a851920c
