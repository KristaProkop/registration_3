from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^modals/(?P<string_path>[\w\-]+)/',views.myView, name="myView"),
]
