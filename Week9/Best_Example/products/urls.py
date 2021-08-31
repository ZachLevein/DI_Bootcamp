from django.contrib import admin
from django.urls import include, path
from. import views


urlpatterns=[
    path('product/', views.product_detail_view, name='product_detail'),
    path('create/', views.product_create_view, name='product_create'),
    path('render/', views.render_initial_data, name='product_create')


]

