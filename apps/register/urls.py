from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
   
    url(r'^modals/(?P<string_path>[\w\-]+)/',views.myView, name="myView"),
    # url(r'^register$', views.register, name='register'),
    # url(r'^testing$', views.testing, name='testing'),
]
