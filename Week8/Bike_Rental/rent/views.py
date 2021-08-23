from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', {"customers":customers})

def vehicles(request):
    vehicles = Vehicle.objects.order_by('size')
    return render(request, 'vehicles.html', {"vehicles":vehicles})

def rentals(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals.html', {"rentals":rentals})



def add_customers(request):
    customers = Customer.objects.all()
    if request.method=='GET':
        form = add_customer()
        print(form.data)
    elif request.method=='POST':
        form = add_customer(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Customer.objects.create(**form.cleaned_data)
    return render(request, 'add_customer.html', {'form': form, 'customers': customers})


def add_vehicles(request):
    vehicles = Vehicle.objects.all()
    if request.method=='GET':
        form = add_vehicle()
        print(form.data)
    elif request.method=='POST':
        form = add_vehicle(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Vehicle.objects.create(**form.cleaned_data)
    return render(request, 'add_vehicle.html', {'form': form, 'vehicles': vehicles})

def add_rentals(request):
    rentals = Rental.objects.all()
    if request.method=='GET':
        form = add_rental()
        print(form.data)
    elif request.method=='POST':
        form = add_rental(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Rental.objects.create(**form.cleaned_data)
    return render(request, 'add_rental.html', {'form': form, 'rentals': rentals})
