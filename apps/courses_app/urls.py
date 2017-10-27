from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$',views.index),
    url(r'^add$',views.add),
    url(r'^(?P<id>\d+)/destroy$',views.destroy),
    url(r'^(?P<id>\d+)/delete$',views.delete)

]