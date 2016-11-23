from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):    
    book_author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    img = models.ImageField(upload_to='blog/static')
    ordered = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title# Create your models here.
class Book_User(models.Model):
	user=models.CharField(max_length=200)
	book=models.IntegerField()
	number=models.IntegerField()
