""" Module for defining the URL patterns for the activities app. """

from django.urls import path

from . import views

urlpatterns = [
    path("rule_count/", views.rule_count, name="rule_count"),
    path("log_list/", views.log_list, name="log_list"),
]
