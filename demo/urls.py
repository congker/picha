from django.conf.urls import include,url,patterns
# from demo.views import test
urlpatterns =patterns('demo.views',
    url(r'^$', 'test', name="test"),

)
