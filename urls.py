from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post(?P<blog_id>[0-9]+)/$',views.b_detail,name='b_detail'),
	# url(r'like/$', views.like_product, name='dict'),
    url(r'blogform/$', views.create_blog, name='blogform'),
    url(r'comment/$', views.comment_product, name='comment'),
]
