from django.urls import path
from . import views

app_name = "app_base" # namespace for app_base 
# <a href=" {% url 'app_base:index_view_name' %} ">index</a>

urlpatterns = [
    path("",views.index_view,name="index_view_name"),
]
