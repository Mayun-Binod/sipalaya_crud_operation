from django.urls import path
from crud_app import views
urlpatterns = [
    path("",views.home,name="home"),
    path("form/",views.form,name="form"),
]