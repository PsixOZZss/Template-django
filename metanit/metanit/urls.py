from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('', views.index),
    path("user/", views.user),
    path("set/", views.set),
    path("userform/", views.userform),
]
