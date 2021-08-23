from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.index, name='index' )
    path('customers/', views.customers, name='customers' ),
    path('customers/add', views.add_customers, name='add_customers' ),

    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/add/', views.add_vehicles, name='add_vehicles'),

    path('rentals/', views.rentals, name='rentals'),
    path('rentals/add/', views.add_rentals, name='add_rentals')


]



# ]    path('person/<int:person_id>', views.person_view, name='person' ),
