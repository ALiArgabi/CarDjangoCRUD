from django.urls import path
from . import views

urlpatterns = [
    #urls for the homepage
    path('', views.index),

    path('ali', views.ali),

]