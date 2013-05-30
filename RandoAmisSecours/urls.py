# -*- coding: utf-8 -*-
# vim: set ts=4

from django.conf.urls import patterns, url

# Main page
urlpatterns = patterns('RandoAmisSecours.views.main',
    url(r'^$', 'index', name='index'),
)

# Authentication
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', {'template_name': 'RandoAmisSecours/registration/login.html'}, name='accounts.login'),
)

# Outing
urlpatterns += patterns('RandoAmisSecours.views.outing',
    url(r'^outings$', 'index', name='outings.index'),
    url(r'^outings/(?P<outing_id>\d+)$', 'details', name='outings.details'),
)
