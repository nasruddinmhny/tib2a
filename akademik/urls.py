from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('manage_mahasiswa/',views.manage_mahasiswa,name='manage_mahasiswa'),
    path('add_mahasiswa/',views.add_mahasiswa,name='add_mahasiswa'),
]
