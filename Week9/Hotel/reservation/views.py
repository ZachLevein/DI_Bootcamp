from django.forms.utils import ErrorList
from django.http.response import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy

import datetime 
from datetime import date
from calendar import monthrange



def homepage(request):
    return render(request, 'partials/home.html')

class BookingDetailView(DetailView):
    model = Booking
class BookingListView(ListView):
    model = Booking

class BookingCreateView(CreateView):
    form_class = BookingForm
    queryset = Booking.objects.all()
    template_name = 'reservation/reservation_create.html'

    def form_valid(self, form):
        # print(form.cleaned_data)
        arrives = form.cleaned_data.get('check_in')
        leaves = form.cleaned_data.get('check_out')
        delta = leaves - arrives 
        updated_spots_pm = 31 - delta.days
        
        date_booked_list = [arrives- datetime.timedelta(days=i) for i in range(delta.days)]

        booked = False
        if not arrives in date_booked_list:
            booked = True
        else: 
            booked = False
            if booked == True:
                print(form.cleaned_data)
                return  super().form_valid(form)
            else:
                return redirect ('home')

    def get_success_url(self):
        return reverse_lazy('reservation_detail', kwargs={'pk':self.object.id})


        