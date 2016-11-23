from django.forms import ModelForm
from blog.models import Post
from django import forms
from django.db import models
from django.forms import ModelForm
class BookForm(ModelForm):
	class Meta:
		model=Post
		fields = ['book_author','title','text','img']
