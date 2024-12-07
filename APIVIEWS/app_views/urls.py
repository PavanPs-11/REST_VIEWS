from django.urls import path

from app_views import views

urlpatterns=[
    path("",views.home),
    path("home1",views.home2)
]