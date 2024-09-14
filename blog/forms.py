from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields  = ['text']     

class SignUpForm(UserCreationForm):
    class Meta:
        model = User    
        fields = ['username', 'password1', 'password2']    