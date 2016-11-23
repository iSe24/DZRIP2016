from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.books, name='bookexmp'),
    url(r'^test/', views.test, name='siteshab'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^addtoorder/(?P<pk>\d+)/$',views.addtoorder, name='addtoorder'),
    url(r'^page/(\d+)/$',views.post_list),
    url(r'^edit/$', views.add)

]
