from django.urls import path
from . import views

urlpatterns = [
    path('vinyls/', views.vinyl_list, name='vinyl_list'),
    path('vinyls/<int:pk>/', views.vinyl_detail, name='vinyl_detail'),
]
