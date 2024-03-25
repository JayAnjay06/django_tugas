from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def dasbor(request):
    return render(request, 'dasbor/dasbor.html')