from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("form/",form,name="form"),
    path("contact/",contact,name="contact"),
    path("about/",about,name="about"),
    path("delete/<int:id>",delete_data,name="delete_data"),
    path("edit/<int:id>",edit,name="edit")
]

