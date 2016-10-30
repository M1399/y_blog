from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	author = models.CharField(max_length=200)
	article_title = models.CharField(max_length=200)
	article_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Comment(models.Model):
	article = models.ForeignKey(Article)
	comment_text = models.CharField(max_length=200)
	comment_author = models.CharField(max_length=200)

class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	passwordQ1 = models.CharField(max_length=200)
	passwordA1 = models.CharField(max_length=200)
	passwordQ2 = models.CharField(max_length=200)
	passwordA2 = models.CharField(max_length=200)
	passwordQ3 = models.CharField(max_length=200)
	passwordA3 = models.CharField(max_length=200)