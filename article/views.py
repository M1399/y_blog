# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包
from article.models import User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import PostForm
from article.models import Post
import pdb

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='密码',widget=forms.PasswordInput())



# Create your views here.

#def detail(request, my_args):
 #   post = Article.objects.all()[int(my_args)]
#    str = ("title = %s, category = %s, date_time = %s, content = %s" 
#        % (post.title, post.category, post.date_time, post.content))
#    return HttpResponse(str)

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})

def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :#未实现
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

#分页

def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 2) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})


class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    #def item_pubdate(self, item):
        #return item.add_date

    def item_description(self, item):
        return item.content
#注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            #将表单写入数据库
            user = User()
            user.username = username
            user.passworld = passworld
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf}, context_instance=RequestContext(request))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#def post(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'post.html', {'post': post})

#class ArticleForm(forms.ModelForm):

#    class Meta:
 #       model = Article
 #       fields = ('title', 'text',)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

	    title = form.cleaned_data['title']
            category = form.cleaned_data['category']
	    content = form.cleaned_data['content']
	    #text = form.cleaned_data['text']
            #将表单写入数据库
	    #global Post
	    pdb.set_trace()
            post = Post
            post.title = title
            post.category = category
	    post.content = content
	    #post.text = text

            Post = form.save(commit=False)
            Post.save()
            return redirect('detail', id=Post.id)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form, 'is_new': True})
