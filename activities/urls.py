""" Module for defining the URL patterns for the activities app. """

from django.urls import path

from . import views

urlpatterns = [
    path("rules/", views.get_rules, name="get_rules"),
    path("log_list/", views.log_list, name="log_list"),
]
