from django.shortcuts import render

def daftar(request):
    return render(request, 'daftar/daftar.html')