from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from apps.slamitsaas import views 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard/dashboard.html')),
    url(r'^diary$', TemplateView.as_view(template_name='diary/diary.html'))
)
