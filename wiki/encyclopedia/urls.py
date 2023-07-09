from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("edit", views.edit, name="edit"), 
    path("update", views.update, name="update"),
    path("randomEntry", views.randomEntry, name="randomEntry"),
    path("add", views.add, name="add"),
    path("wiki/<str:entry>", views.entryPage, name="entryPage"),
]
