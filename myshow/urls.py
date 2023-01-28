from django.urls import path
from . import views


urlpatterns = [
    path('',views.login_user,name='login'),
    path('index',views.index,name='index'),
    path('regsiter',views.regsiter , name = 'register'),
    path('movies',views.movies,name='movies'),
    path('logout',views.user_logout,name='logout'),
    path('gifts',views.gifts,name='gifts'),
    path('movie_page/<movie_number>',views.movie_page,name="movie_page"),
]