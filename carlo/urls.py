# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'carlo'
urlpatterns = [
    path('group', views.IndexView.as_view(), name='index'),
    path('group/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('group/<int:pk>/member_list', views.DetailView.as_view(), name='member_list'),
]