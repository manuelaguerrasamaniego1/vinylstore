from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Vinyl
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

# Widok listy winyli
def vinyl_list(request):
    """
    Widok zwracający listę wszystkich winyli.
    """
    vinyls = Vinyl.objects.all()  # Pobierz wszystkie obiekty z modelu Vinyl
    return render(request, 'shop/vinyl_list.html', {'vinyls': vinyls})

# Widok szczegółowy dla pojedynczego winyla
def vinyl_detail(request, pk):
    """
    Widok szczegółowy dla pojedynczego winyla.
    """
    vinyl = get_object_or_404(Vinyl, pk=pk)  # Pobierz obiekt lub zwróć 404
    return render(request, 'shop/vinyl_detail.html', {'vinyl': vinyl})

# Widok edycji winyla
class VinylUpdateView(UpdateView):
    model = Vinyl
    fields = ['title', 'artist', 'genre', 'release_year', 'price']
    template_name = 'shop/vinyl_edit.html'
    success_url = reverse_lazy('vinyl_list')  # Po edycji wraca na listę winyli

# Widok usuwania winyla
class VinylDeleteView(DeleteView):
    model = Vinyl
    template_name = 'shop/vinyl_delete.html'
    success_url = reverse_lazy('vinyl_list')  # Po usunięciu wraca na listę winyli
