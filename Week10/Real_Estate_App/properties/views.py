from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.urls import reverse_lazy
from .filters import *


class HomePage(TemplateView):
    template_name = "partials/home.html"
    properties = Property.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        return context 


class PropertyDetailView(DetailView):
    model = Property

class PropertyListView(ListView):
    model = Property
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        return context 
    
    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)
        context['filter'] = PropertyFilter(self.request.GET, queryset=self.get_queryset())
        return context


def PropertySearch(request):
    if request.method == "POST":
        searched = request.POST['searched'].capitalize()
        properties = Property.objects.filter(city__contains= searched)

        
        return render(request, 'properties/property_search.html', {"searched": searched, "properties": properties})


    # return render(request, 'properties/property_search.html', {})

def search(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    
    return render(request,'properties/property_list.html', {"filter": property_filter} )




