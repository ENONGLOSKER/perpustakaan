from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group, Permission

# Create your views here.
def index(request):
    return render(request, 'index.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Password tidak sama!")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            group = Group.objects.get(name='tamu')  # Ganti 'staf' dengan nama grup yang sesuai
            my_user.groups.add(group)
            permission = Permission.objects.get(codename='is_staff')  # Ganti 'is_staff' dengan kode nama izin yang sesuai
            my_user.is_staff = True
            my_user.user_permissions.add(permission)
            my_user.save()
            messages.success(request, "Selamat, Register Berhasil!")
            return redirect('/')

    return render(request, 'signup.html')
