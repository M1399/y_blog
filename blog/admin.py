from django.contrib import admin

from .models import Article, Comment, User

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'author', 'pub_date')
    search_fields = ['article_title']
    # inlines = [CommentInline]
    fieldsets = [
        ('article information', {'fields': ['article_title', 'article_text', 'author']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(Article, ArticleAdmin)

class CommentInline(admin.ModelAdmin):
    list_display = ('comment_text', 'comment_author', 'article')
    search_fields = ['comment_text']
    fieldsets = [
        ('comment information', {'fields': ['comment_text', 'comment_author', 'article']}),
    ]
admin.site.register(Comment, CommentInline)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'passwordQ1', 'passwordA1', 'passwordQ2', 'passwordA2', 'passwordQ3', 'passwordA3')
    search_fields = ['article_title']
    fieldsets = [
        (None, {'fields': ['username', 'password', 'passwordQ1', 'passwordA1', 'passwordQ2', 'passwordA2', 'passwordQ3', 'passwordA3']}),
    ]
admin.site.register(User, UserAdmin)