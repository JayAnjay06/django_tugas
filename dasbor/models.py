from django.db import models

class Penerbit(models.Model):
    nama = models.CharField(max_length=100)
    # Tambahkan informasi lain yang Anda butuhkan

    def __str__(self):
        return self.nama

class Pengarang(models.Model):
    nama = models.CharField(max_length=100)
    # Tambahkan informasi lain yang Anda butuhkan

    def __str__(self):
        return self.nama

class RakBuku(models.Model):
    nama = models.CharField(max_length=100)
    # Tambahkan informasi lain yang Anda butuhkan

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.ForeignKey(Pengarang, on_delete=models.CASCADE, null=True)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE, null=True)
    rak = models.ForeignKey(RakBuku, on_delete=models.CASCADE, null=True)
    # Tambahkan informasi lain yang Anda butuhkan

    def __str__(self):
        return self.judul

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    # Tambahkan informasi lain yang Anda butuhkan

    def __str__(self):
        return self.nama
