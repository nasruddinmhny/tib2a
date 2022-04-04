from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_akademik, name='akademik_dashboard'),
    path('add_akademik/',views.add_akademik,name='add_akademik')
]
