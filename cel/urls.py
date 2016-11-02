from django.conf.urls import url,patterns,include
from django.contrib import admin
# from picha.views import hello,my

urlpatterns =patterns('cel.views',
  # url(r'', include('picha.urls')),
  #  url(r'^admin/', admin.site.urls),
   # url(r'^demo/$', include('demo.urls')),
   url(r'^$','testCelery'),
   # url('^hello/$', 'hello'),
)