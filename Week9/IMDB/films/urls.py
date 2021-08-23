from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_film', views.add_film, name='add_film'),
    path('create_film', views.FilmCreateView.as_view(), name = 'title'),
    path('show_films', views.FilmListView.as_view(), name = 'all_films'),
    path('show_films/<int:pk>', views.FilmDetailView.as_view(), name = 'film_detail'),

]