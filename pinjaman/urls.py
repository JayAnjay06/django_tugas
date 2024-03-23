from django.urls import path
from . import views


urlpatterns = [
    path('', views.pinjaman, name='pinjaman'),
]