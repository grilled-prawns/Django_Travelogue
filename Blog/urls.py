
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/' , include('blog_app.urls')),
    url(r'^sign_up/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'blog_app/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'blog_app/index.html'}, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

