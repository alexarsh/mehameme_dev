from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^popup_test/', 'main.views.popup_test', name='popup_test'),
)
