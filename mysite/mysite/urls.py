from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, queries, query1, query2, query3

urlpatterns = patterns('',
    url(r'^queries/$', queries),
    url(r'^query1/$', query1),
    url(r'^query2/$', query2),
    url(r'^query3/$', query3),
    url(r'^$', home),
)
