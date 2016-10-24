# -*- coding: utf-8 -*- 
from django import forms
from article.models import Post ##
from .models import Post,Article,BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        """指定一些 Meta 选项以改变 form 被渲染后的样式"""
        model = BlogComment # form 关联的 Model

        fields = ['user_name', 'user_email', 'body']
       
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.Textarea(attrs={'placeholder': '我来评两句~'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__" 
       # fields = ('title', 'text')
        labels = {
            'text': '正文',
            'title': '标题',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 15}),
        }


