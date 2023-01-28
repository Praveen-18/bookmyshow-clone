from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myshow/index.html')

def movie_page(request,movie_name):
    print(movie_name)
    return render(request,'myshow/movie_page.html',{'movie_name':movie_name})