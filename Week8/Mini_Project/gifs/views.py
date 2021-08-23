from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import Gif_Form



def index(request):
    # cars = get_list_or_404(Vehicle, color='red')
    gifs = Gif_Model.objects.all()
    return render(request, 'index.html', {'gifs':gifs})


def home(request):    
  context = {"home_page": "active"} # new info here    
  return render(request, 'gifs/index.html', context)

def admin(request):    
  context = {"admin_page": "active"} # new info here    
  return render(request, 'admin', context)


def add_form(request):
  gifs = Gif_Model.objects.all()
  
  if request.method=='GET':
    form= Gif_Form()
  
  elif request.method=='POST':
    form = Gif_Form(request.POST)
    print(form.data)
    
    if form.is_valid():
      print(form.cleaned_data)
      Gif_Model.objects.create(**form.cleaned_data)
  
  
  
  return render(request, 'add_form.html', {'form':form, 'gifs': gifs})
