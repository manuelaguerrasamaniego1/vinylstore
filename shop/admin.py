from django.contrib import admin
from .models import Vinyl, Order, OrderItem

# Rejestracja modeli w panelu admina
@admin.register(Vinyl)
class VinylAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'release_year', 'price', 'stock')  # Wyświetlane kolumny
    search_fields = ('title', 'artist')  # Możliwość wyszukiwania po tytule i artyście

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total_price')  # Wyświetlane kolumny
    list_filter = ('status', 'created_at')  # Filtrowanie po statusie i dacie
    search_fields = ('user__username',)  # Wyszukiwanie po nazwie użytkownika

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'vinyl', 'quantity')  # Wyświetlane kolumny
