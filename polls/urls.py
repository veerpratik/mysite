from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name ='index' ), # by default this page will be open index and in which called function whos name is infdex
]