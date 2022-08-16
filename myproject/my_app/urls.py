from django.urls import path #allow us to configure all paths
from . import views

urlpatterns = [
    path('homepage/', views.index, name="index")
]