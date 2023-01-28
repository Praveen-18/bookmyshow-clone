from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_user,name='login'),
    path('regsiter',views.regsiter , name = 'register'),
    path('movie_page/<movie_number>',views.movie_page,name="movie_page"),
]