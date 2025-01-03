from django.urls import path
from crud_app import views
urlpatterns = [
    path("",views.home,name="home"),
    path("form/",views.form,name="form"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("delete/<int:id>/",views.delete_data,name="delete_data"),

]
