from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from .forms import UserForm
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login

# Create your views here.

def index(request):
    context = {}
    return render(request, 'accounts/index.html', context)

def contact(request):
    context = {}
    return render(request, 'accounts/contact.html', context)

def about(request):
    context = {}
    return render(request, 'accounts/about.html', context)

def loginView(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid login credentials')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    context = {'page': page}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('index')
    
def registerPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(
            request, "Unsuccessful registration, please valid credentials!!!")
    form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form": form})
