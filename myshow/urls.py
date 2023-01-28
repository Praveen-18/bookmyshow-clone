from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('regsiter',views.regsiter , name = 'register'),
    path('movie_page/<movie_name>',views.movie_page,name="movie_page"),
]