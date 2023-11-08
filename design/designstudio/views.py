from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import login as dj_login
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'photo_file']
    template_name = 'main_request.html'
    success_url = reverse_lazy('my_request')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def request_main(request):
    return render(request, "main_request.html",)


class MyPostListViews(generic.ListView):
    model = Application
    context_object_name = 'application'
    template_name = 'my_request.html'




    def get_queryset(self):
        return Application.objects.filter(user=self.request.user).order_by('-date')


class ApplicationDelete(DeleteView):
    model = Application
    context_object_name = 'application'
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('my_request')

class ApplicationListViewAdmin(generic.ListView):
    model = Application
    template_name = 'base.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Application.objects.order_by('-date')[:4]




class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'base.html'