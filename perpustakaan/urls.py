from django.contrib import admin
from django.urls import path, include

from masuk import views
from daftar import views as Daftar
from pinjaman import views as Pinjaman

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('masuk.urls')),
    path('daftar/', include('daftar.urls')),
    path('pinjaman', include('pinjaman.urls')),
]
