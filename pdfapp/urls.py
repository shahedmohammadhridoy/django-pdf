from django.urls import path
from . import views

urlpatterns = [
    path('download', views.getpdf, name='pdf'),
]
