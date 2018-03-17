from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_update, name='update_post'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='delete_post'),

]