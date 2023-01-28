from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import user
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'myshow/index.html')

def movie_page(request,movie_number):

    print(movie_number)
    ini_path="myshow/images/recommendedMovies/image"+movie_number+".png"
    return render(request,'myshow/movie_page.html',{'movie_path':ini_path})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        curr_user = authenticate(username=email, password=password)
        if curr_user is not None:
            login(request,curr_user)
            return redirect('/')
        else:
            return render(request, 'myshow/login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request , 'myshow/login.html')

def regsiter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        password = request.POST.get('pass')
        Curruser = user(name=name, email=email, phone=phone)
        authUser = User.objects.create_user(name, email, password)
        authUser.save()
        Curruser.save()
        return redirect('/login')
    else:
        return render(request , 'myshow/register.html')

