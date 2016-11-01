from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.books, name='bookexmp'),
    url(r'^test/', views.test, name='siteshab'),
]
