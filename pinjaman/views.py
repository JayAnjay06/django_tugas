from django.shortcuts import render

def pinjaman(request):
    return render(request, 'pinjaman/pinjaman.html')