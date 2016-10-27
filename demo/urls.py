from django.conf.urls import include,url,patterns
from demo.views import test
urlpatterns =patterns('',
    'r^&',test,
    #'^test/$','test'
)
