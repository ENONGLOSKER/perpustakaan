from django.contrib import admin
from .models import Kategori, Buku, Anggota, Peminjaman, Petugas
from django.contrib.auth.models import Permission

class CustomModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Hanya tampilkan data jika status izin adalah 'active'
            qs = qs.filter(anggota__user=request.user, anggota__user__is_active=True)
        return qs

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser and not request.user.has_perm('perpustakaan_app.change_anggota'):
            # Hanya izinkan perubahan jika status izin adalah 'active'
            return False
        return True


# Register your models here.
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul','penulis','tahun_terbit','kategori')
    list_filter = ['judul','penulis','tahun_terbit','kategori']
class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('user','alamat','nomor_telepon')
    list_filter = ['user','alamat','nomor_telepon']
class PeminjamAdmin(admin.ModelAdmin):
    list_display = ('buku','anggota','tanggal_peminjaman','tanggal_pengembalian','status')
class PetugasAdmin(admin.ModelAdmin):
    list_display = ('user','posisi')
    list_filter = ['user','posisi']

admin.site.register(Buku,BukuAdmin)
admin.site.register(Anggota,AnggotaAdmin)
admin.site.register(Peminjaman,PeminjamAdmin)
admin.site.register(Petugas,PetugasAdmin)
admin.site.register(Kategori)