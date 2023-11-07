from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import login as dj_login
from .forms import LoginForm
from django.contrib.auth import authenticate

from .forms import Registration

from .models import CustomUser, Application


def base(request):
    return render(request, "base.html",)

def personalarea(request):
    return render(request, "personalarea.html",)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('personalarea')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})

def logout(request):
    return render(request, "logout.html")

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username, email, password)
            user.first_name = full_name
            user.save()
            dj_login(request, user)
            return redirect('base')
    else:
        form = Registration()
    return render(request, 'registration/register.html', {'form': form})

class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'base.html'