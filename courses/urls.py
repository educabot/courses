__author__ = 'diegoram'

from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )