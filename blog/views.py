# -*- coding: utf-8 -*-

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Article, Comment, User

import pdb


def index(request):
    username = request.session.get('username', 'visitor')
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
        'user': username
    }
    return HttpResponse(template.render(context, request))

def login(request):
	pass

def register(request):
	pass

def addArticle(request):
    context = {}
    template = loader.get_template('blog/addArticle.html')
    return HttpResponse(template.render(context, request))

def showArticle(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)

def delArticle(request, article_id):
    # TODO del 
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))

def addComment(request):
	pass

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
                return render(request, 'blog/changePassword.html', {'error':error})
            else:
                if newPassword == newPasswordAgain:
                    userSQL.password = newPassword
                    userSQL.save()
                    ok = '修改密码成功'
                    return render(request, 'blog/changePassword.html', {'ok':ok})
                else:
                    error = '两次密码输入不相同'
                    return render(request, 'blog/changePassword.html', {'error':error})
        else:
            return render(request, 'blog/changePassword.html', {'uf':form})
    else:
        uf = UserFormForChange()
    return render(request,'blog/changePassword.html', {'username':username, 'uf':uf})


# 登出
def logout(request):
    if request.session.get('username'):
        del request.session['username']
    return HttpResponse('logout ok!')