
# -*- coding: utf-8 -*-
import settings
"""y_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import home,detail,archives,about_me,blog_search,RSSFeed
from article.views import register,login,index,logout,post_new
from django.views import static
#from . import views


admin.autodiscover()

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),  #可以使用设置好的url进入网站后台
    #url(r'^$', 'article.views.home'),
    #url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
  
    url( r'^static/(?P<path>.*)$', static.serve,
                                            { 'document_root':settings.STATIC_URL }),
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^article/', include(article.urls)),
   # url(r'^register/$',register,name='register'),
    #url(r'^$', login, name='login'),
    url(r'^login/$',login,name = 'login'),
    url(r'^register/$',register,name = 'register'),
    url(r'^index/$',index,name = 'index'),
    url(r'^logout/$',logout,name = 'logout'),
    url(r'^new/$', post_new, name='post_new'),

    url(r'^$', home, name='home'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives, name = 'archives'),
    url(r'^aboutme/$', about_me, name = 'about_me'),
   # url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
    url(r'^search/$',blog_search, name = 'search'),
    url(r'^Feed/$', RSSFeed(), name = "RSS"),
]
