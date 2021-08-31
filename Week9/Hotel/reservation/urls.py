from django.contrib import admin
from django.urls import include, path
from. import views


urlpatterns=[
    path('', views.homepage, name='home'),
    path('booking/create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/all/', views.BookingListView.as_view(), name='all_bookings'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='reservation_detail'),


]