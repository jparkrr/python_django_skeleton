from django.conf.urls import patterns, url
urlpatterns = patterns('singly.views',
    url(r'^authenticate/(?P<service>[a-z]+)/$', 'authenticate_redirect',
        name='authenticate_redirect'),
    url(r'^authorize/callback/$', 'authorize_callback',
        name='authorize_callback')
)
