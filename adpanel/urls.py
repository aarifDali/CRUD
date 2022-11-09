from unicodedata import name
from django.contrib import admin
from django.urls import path
from adpanel import views


urlpatterns = [
    path('userdisplay/', views.userdisplay, name="userdisplay"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('search', views.search_username, name="searchusername")
]