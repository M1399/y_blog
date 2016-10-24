from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article, Comment, User


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
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