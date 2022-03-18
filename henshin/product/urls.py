from django.contrib import admin
from django.urls import path

from . import views

app_name = "productos"
urlpatterns = [
    path("", views.IndexView.as_view(), name = 'index'),
    
    # path("", views.index, name = 'index'),

]
