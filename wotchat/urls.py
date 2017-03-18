from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, URLRedirectView, RedirectToEmailcheckView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    # url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'), 
    url(r'^res/(?P<shortcode>[\w-]+)/$', RedirectToEmailcheckView.as_view(), name='scode'), 
]
