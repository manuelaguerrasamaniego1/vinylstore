from django.urls import path
from . import views

urlpatterns = [
    path('', views.vinyl_list, name='vinyl_list'),  # Używamy funkcji vinyl_list
    path('vinyls/<int:pk>/', views.vinyl_detail, name='vinyl_detail'),  # Używamy funkcji vinyl_detail
    path('vinyls/<int:pk>/edit/', views.VinylUpdateView.as_view(), name='vinyl_edit'),
    path('vinyls/<int:pk>/delete/', views.VinylDeleteView.as_view(), name='vinyl_delete'),
]
