from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.forms import modelformset_factory, inlineformset_factory




def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {'films':films})

# CREATE
@login_required
def add_film(request):
    films = Film.objects.all()
    if request.method == 'GET':
        form = FilmForm()
    elif request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save(commit=False)
            film.created_by = request.user.profile
            film.save()
            return redirect('home')

    return render(request, 'add_page.html', {'films': films, 'form':form,'title':'Add Film', 'obj_type':'Film'})

class FilmListView(ListView):
    model = Film
    ordering = '-title'

class FilmDetailView(DetailView):
    model = Film
    

class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film.objects.all()
    # fields = '__all__'
    form_class = FilmForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('all_films')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = 'first_name'
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['director'].queryset = Director.objects.filter(title__istartswith='A')
        form.fields['country'].queryset = Country.objects.filter(title__istartswith='A')
    
        return form
    
    def form_valid(self, form):
        film = form.save(commit=False)
        film.created_by = self.request.user.profile
        film.save()
        return super().form_valid(form)

# class AnimalUpdateView(LoginRequiredMixin,UpdateView):
#     model = Film
#     fields = '__all__'
#     # form_class = AnimalForm
#     template_name = 'add_page.html'
#     success_url = reverse_lazy('all_films')

