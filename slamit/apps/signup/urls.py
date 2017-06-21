from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from apps.signup import views





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^signup/$', views.signup, name="signup"),
     url(r'signin/$', views.login_user, name="auth_login"),
     url(r'^$', TemplateView.as_view(template_name='login/launching.html')),
    
)
