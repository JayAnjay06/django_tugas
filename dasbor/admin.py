from django.contrib import admin
from .models import Penerbit, Pengarang, RakBuku, Buku, Anggota

@admin.register(Penerbit)
class PenerbitAdmin(admin.ModelAdmin):
    list_display = ('nama',)

@admin.register(Pengarang)
class PengarangAdmin(admin.ModelAdmin):
    list_display = ('nama',)

@admin.register(RakBuku)
class RakBukuAdmin(admin.ModelAdmin):
    list_display = ('nama',)

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pengarang', 'penerbit', 'rak')
    list_filter = ('pengarang', 'penerbit', 'rak')
    search_fields = ['judul']

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('nama',)
