from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('movie_page/<movie_name>',views.movie_page,name="movie_page"),
]