from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'(?P<num>[a-z]+)^$', views.index),
    url(r'^$', views.index, name="index"),
    #url(r'^blog/$', views.page),
    #url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

#def index(request, num="1"):
#    if(num!="1"):
#        print(num)
