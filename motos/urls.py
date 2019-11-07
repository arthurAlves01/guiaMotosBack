from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$','motos.views.index', name='home'),
    url(r'^motos$', 'motos.views.exibir', name='exibir'),
    url(r'^login$', 'motos.views.login', name='login'),
    url(r'^cadastra$', 'motos.views.cadastrar', name='cadastrar')
)