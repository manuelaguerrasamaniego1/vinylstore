from django.shortcuts import render
from .models import Vinyl

def vinyl_list(request):
    """
    Widok zwracający listę wszystkich winyli.
    """
    vinyls = Vinyl.objects.all()  # Pobierz wszystkie obiekty z modelu Vinyl
    return render(request, 'shop/vinyl_list.html', {'vinyls': vinyls})
