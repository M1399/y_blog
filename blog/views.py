from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Comment, User


def index(request):
    latest_question_list = Article.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.article_title for p in latest_question_list])
    return HttpResponse(output)
    return HttpResponse("Hello, world. You're at the blog index.")

def login(request):
	pass

def register(request):
	pass

def addArticle(request):
	pass

def showArticle(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)

def addComment(request):
	pass