from django.urls import path
from app_imc.views import index

urlpatterns = [
    path('index/', index),
]