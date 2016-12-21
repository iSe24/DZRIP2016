from blog.models import Post
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Post
        fields = ['book_author', 'title', 'text', 'img']
