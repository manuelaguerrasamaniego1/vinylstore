from django.shortcuts import render, get_list_or_404
from .models import Vinyl

def vinyl_list(request):
    """
    Widok zwracający listę wszystkich winyli.
    """
    vinyls = Vinyl.objects.all()  # Pobierz wszystkie obiekty z modelu Vinyl
    return render(request, 'shop/vinyl_list.html', {'vinyls': vinyls})

def vinyl_detail(request, pk):
    """
    Widok szczegółowy dla pojedynczego winyla.
    """
    vinyl = get_object_or_404(Vinyl, pk=pk)  # Pobierz obiekt lub zwróć 404
    return render(request, 'shop/vinyl_detail.html', {'vinyl': vinyl})