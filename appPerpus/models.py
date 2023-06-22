from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul


class Anggota(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.CharField(max_length=200)
    nomor_telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    tanggal_peminjaman = models.DateField()
    tanggal_pengembalian = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.anggota.user.username} - {self.buku.judul}"


class Petugas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posisi = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
