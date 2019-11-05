from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$','motos.views.index'),
    url(r'motos$', 'motos.view.exibir')
)
