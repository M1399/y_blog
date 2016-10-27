from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.index, name='index'),
    url(r'^blogs$', views.blogs, name='blogs'),
    url(r'^blogsByAjax$', views.blogsByAjax, name='blogsByAjax'),
    url(r'^blog/(?P<article_id>[0-9]+)/$', views.showArticle, name='showArticle'),
    url(r'^blog/(?P<article_id>[0-9]+)/del$', views.delArticle, name='delArticle'),
    url(r'^blog/(?P<article_id>[0-9]+)/dels$', views.delArticles, name='delArticles'),
    url(r'^blog/addArticle/', views.addArticle, name='addArticle'),
    url(r'^blog/addArticleByAjax', views.addArticleByAjax, name='addArticleByAjax'),
    # url(r'^login/', views.login, name='login'),
    # url(r'^register/', views.register, name='register'),

    # url(r'^showArticle/', views.showArticle, name='showArticle'),
    # url(r'^addComment/', views.addComment, name='addComment'),
]