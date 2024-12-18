from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect 
from .models import Vinyl
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.db.models import Q


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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Automatycznie logujemy użytkownika po rejestracji
            return redirect('vinyl_list')  # Po rejestracji przekierowanie na stronę listy winyli
    else:
        form = UserRegistrationForm()

    return render(request, 'shop/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('vinyl_list')  # Po zalogowaniu przekierowanie na stronę z winylami
    else:
        form = AuthenticationForm()

    return render(request, 'shop/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('vinyl_list')

def vinyls_by_genre(request, genre):
    """
    Widok zwracający listę winyli dla podanego gatunku muzycznego.
    """
    vinyls = Vinyl.objects.filter(genre__icontains=genre)
    return render(request, 'shop/vinyls_by_genre.html', {'vinyls': vinyls, 'genre': genre})

def vinyls_by_year(request, year):
    """
    Widok zwracający listę winyli wydanych w podanym roku.
    """
    vinyls = Vinyl.objects.filter(release_year=year)
    return render(request, 'shop/vinyls_by_year.html', {'vinyls': vinyls, 'year': year})




