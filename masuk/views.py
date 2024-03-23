from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin

def index(request):
    form = FormLogin()
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('/login/beranda')

    return render(request, 'index.html',{'form':form})