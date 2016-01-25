from django.conf.urls import patterns, include, url
from apps.slamitsaas import views 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', views.login, name='login_url'),
)
