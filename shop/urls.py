from django.urls import path
from . import views

urlpatterns = [
    path('vinyls/', views.vinyl_list, name='vinyl_list'),
]
