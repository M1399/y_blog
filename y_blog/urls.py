<<<<<<< HEAD

=======
>>>>>>> 9ad492ca599a5059a8186f2e4ffabf56a851920c
# -*- coding: utf-8 -*-

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
<<<<<<< HEAD
from article.views import home,detail,archives,about_me,blog_search,RSSFeed
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),  #可以使用设置好的url进入网站后台
    #url(r'^$', 'article.views.home'),
    #url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives, name = 'archives'),
    url(r'^aboutme/$', about_me, name = 'about_me'),
   # url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
    url(r'^search/$',blog_search, name = 'search'),
    url(r'^Feed/$', RSSFeed(), name = "RSS"),
=======

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),  #可以使用设置好的url进入网站后台
    url(r'^$', 'article.views.home'),
    url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),


>>>>>>> 9ad492ca599a5059a8186f2e4ffabf56a851920c
]
