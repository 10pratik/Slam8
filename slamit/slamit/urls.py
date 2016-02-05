from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.slamitsaas import urls
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^', include('apps.slamitsaas.urls')),
    url(r'^',include('apps.signup.urls')),
    url(r'^',include('apps.slamitsaas.urls')),
)
if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
