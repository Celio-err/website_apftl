from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, "admin_templates/index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Favor Prenxe Username no Password ho loos!")
            return render(request, "admin_templates/auth-login.html")
    return render(request, "admin_templates/auth-login.html")

def logout_view(request):
    logout(request)
    return redirect ('login')

def register_view(request):
    return render(request, "admin_templates/auth-register.html")

def profile_view(request):
    return render(request, "admin_templates/profile.html")