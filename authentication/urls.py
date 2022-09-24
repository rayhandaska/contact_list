# using git commit -m
from django.urls import path
from .views import RegisterView


urlpatterns = [
    path('register', RegisterView.as_view())

]
