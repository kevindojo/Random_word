from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^random_word$', views.index),          #dont forget commas!
    url(r'^generate$', views.generate),           # dont forget commas!!
    url(r'^reset$',views.reset),
]