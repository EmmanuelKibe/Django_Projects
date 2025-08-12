from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", home_view, name='home'),
]
