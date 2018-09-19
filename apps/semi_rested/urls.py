from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$',views.new),
    url(r'^users/create$',views.create)
]