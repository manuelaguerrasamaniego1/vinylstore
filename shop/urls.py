from django.urls import path
from . import views

urlpatterns = [
    path('', views.vinyl_list, name='vinyl_list'),  # Używamy funkcji vinyl_list
    path('vinyls/<int:pk>/', views.vinyl_detail, name='vinyl_detail'),  # Używamy funkcji vinyl_detail
    path('vinyls/<int:pk>/edit/', views.VinylUpdateView.as_view(), name='vinyl_edit'),
    path('vinyls/<int:pk>/delete/', views.VinylDeleteView.as_view(), name='vinyl_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('vinyls/genre/<str:genre>/', views.vinyls_by_genre, name='vinyls_by_genre'),
    path('vinyls/year/<int:year>/', views.vinyls_by_year, name='vinyls_by_year'),
]
