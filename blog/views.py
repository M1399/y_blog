# -*- coding: utf-8 -*-

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from .models import Article, Comment, User

import pdb


# 首页
def index(request):
    username = request.session.get('username', 'visitor')
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
        'user': username
    }
    return HttpResponse(template.render(context, request))


# 添加博客文章
class ArticleFormForAddArticle(forms.Form):
    article_title = forms.CharField(max_length=200)
    article_text = forms.CharField(max_length=200)


# 发帖
def addArticle(request):
    if not request.session.get('username'):
        return HttpResponseRedirect('/login') 
    if request.method == 'POST':
        form = ArticleFormForAddArticle(request.POST)
        if form.is_valid():
            articleSQL = Article()
            articleSQL.article_title = form.cleaned_data['article_title']
            articleSQL.article_text = form.cleaned_data['article_text']
            articleSQL.author = request.session.get('username')
            articleSQL.pub_date = datetime.now()
            articleSQL.save()
            return HttpResponseRedirect('/blog')
        else:
            return render(request, 'blog/addArticle.html', {'uf':form})       
    else:
        form = ArticleFormForAddArticle()
    return render(request, 'blog/addArticle.html', {'uf':form})


# 评论相关的表单
class CommentForm(forms.Form):
    comment_text = forms.CharField(max_length=200)


# 博文详细内容及评论/添加评论的表单
def showArticle(request, article_id):
    article = Article.objects.get(id=article_id)
    comment_all = Comment.objects.filter(article=article)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not request.session.get('username'):
            return HttpResponseRedirect('/login') 
        if form.is_valid():
            commentSQL = Comment()
            commentSQL.article = article
            commentSQL.comment_text = form.cleaned_data['comment_text']
            commentSQL.comment_author = request.session.get('username')
            commentSQL.save()
    else:
        form = CommentForm()
    return render(request, 'blog/showArticle.html', {'uf':form, 'article':article, 'comment_all':comment_all})


# 删除博文
def delArticle(request, article_id):
    # TODO del 
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect('/blog')


# 登陆相关的表单
class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class UserFormForRegister(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    passwordAgain = forms.CharField(max_length=200)   


class UserFormForChange(forms.Form):
    password = forms.CharField(max_length=200)
    newPassword = forms.CharField(max_length=200)
    newPasswordAgain = forms.CharField(max_length=200)   


# 登陆
def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']           
            try:
                userSQL = User.objects.get(username=username, password=password) 
            except User.DoesNotExist:
                error = '用户名或密码错误'
                return render(request, 'blog/login.html', {'error':error}) 
            else:
                request.session['username'] = username
                return HttpResponseRedirect('/blog')
        else:
            return render(request, 'blog/login.html', {'uf':form})
    else:
        uf = UserForm()
    return render(request, 'blog/login.html', {'uf':uf})


# 注册
def register(request):
    if request.method == 'POST':
        form = UserFormForRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            passwordAgain = form.cleaned_data['passwordAgain']
            if password == passwordAgain:
                userSQL = User()
                userSQL.username = username
                userSQL.password = password
                userSQL.save()
                request.session['username'] = username
                return HttpResponseRedirect('/blog')
            else:
                error = '两次密码输入不相同'
                return render(request, 'blog/register.html', {'error':error})
        else:
            return render(request, 'blog/register.html', {'uf':form})
    else:
        uf = UserFormForRegister()
    return render(request,'blog/register.html', {'uf':uf})


# 修改密码
def changePassword(request):
    username = request.session.get('username', 'visitor')
    if(username == 'visitor'):
        return HttpResponse('not logged on')
    if request.method == 'POST':
        form = UserFormForChange(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            newPassword = form.cleaned_data['newPassword']
            newPasswordAgain = form.cleaned_data['newPasswordAgain']
            try:
                userSQL = User.objects.get(username=username, password=password)
            except User.DoesNotExist:
                error = '密码错误'
                return render(request, 'blog/changePassword.html', {'username':username, 'info':error})
            else:
                if newPassword == newPasswordAgain:
                    if password != newPassword:
                        userSQL.password = newPassword
                        userSQL.save()
                        info = '修改密码成功'
                    else:
                        info = '输入的密码和原密码一致'
                else:
                    info = '两次密码输入不相同'
                return render(request, 'blog/changePassword.html', {'username':username, 'info':info})
        else:
            return render(request, 'blog/changePassword.html', {'username':username, 'uf':form})
    else:
        uf = UserFormForChange()
    return render(request,'blog/changePassword.html', {'username':username, 'uf':uf})


# 登出
def logout(request):
    if request.session.get('username'):
        del request.session['username']
    return render(request, 'blog/logout.html')