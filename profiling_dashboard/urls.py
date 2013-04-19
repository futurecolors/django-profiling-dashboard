# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from profiling_dashboard import views


urlpatterns = patterns('',
    url(r'^do$', views.yappi_manage, name='profiling_yappi_manage'),
    url(r'^memory-usage/$', views.memory_usage, name='profiling_memory_usage'),
    url(r'^top/$', views.web_top, name='profiling_web_top'),
    url(r'^top/(?P<pid>\d+)$', views.process_info, name='profiling_process_info'),
    url(r'^$', views.yappi_stats, name='profiling_yappi_stats')
)
