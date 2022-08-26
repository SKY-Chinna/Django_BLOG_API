from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("get/", get),
    path("view/<int:id>",View),
    path("update/<int:id>/",Update),
    path("delete/<int:id>/",delete),
    path("add/",create),


]