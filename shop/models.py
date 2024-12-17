from django.db import models
from django.contrib.auth.models import User  # Domyślny model użytkownika Django

# Model reprezentujący płytę winylową
class Vinyl(models.Model):
    title = models.CharField(max_length=255)  # Tytuł płyty
    artist = models.CharField(max_length=255)  # Artysta
    genre = models.CharField(max_length=100)  # Gatunek muzyczny
    release_year = models.PositiveIntegerField()  # Rok wydania
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Cena
    stock = models.PositiveIntegerField()  # Ilość dostępnych płyt

    def __str__(self):
        return f'{self.title} - {self.artist}'

# Model reprezentujący zamówienie
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Użytkownik (opcjonalnie)
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia zamówienia
    status = models.CharField(max_length=50, default='pending')  # Status zamówienia
    total_price = models.DecimalField(max_digits=8, decimal_places=2)  # Całkowita cena zamówienia

    def __str__(self):
        return f'Order {self.id} by {self.user.username if self.user else "Guest"}'

# Model reprezentujący pozycję w zamówieniu
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)  # Powiązanie z zamówieniem
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)  # Powiązanie z winylem
    quantity = models.PositiveIntegerField()  # Ilość zamówionych płyt

    def __str__(self):
        return f'{self.quantity} x {self.vinyl.title}'
