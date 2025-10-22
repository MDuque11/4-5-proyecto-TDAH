from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import get_user_model

# Create your views here.

def frist_view(request):
    return render(request, 'base.html')

def main_view(request):
    return render(request, 'base.html')



def register(request):
    User = get_user_model()
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not nickname or not email or not password1 or not password2:
            return render(request, 'registration/register.html')

        if password1 != password2:
            return render(request, 'registration/register.html')

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/register.html')

        user = User.objects.create_user(username=email, email=email, password=password1, nickname=nickname)
        user.save()
        return redirect('login')

    return render(request, 'registration/register.html')

def login_view(request):
    User = get_user_model()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'registration/login.html')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')

def exit(request):
    logout(request)
    return redirect('index')
