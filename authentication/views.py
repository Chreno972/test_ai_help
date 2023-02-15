from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def home_page(request):
    return render(request, 'home.html')

def register_page(request):
    """_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('dashboard')
    return render(
        request,
        'registration/register.html',
        context={'form': form},
    )

@login_required
def logout_user(request):
    """_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    logout(request)
    return redirect('home')


def login_page(request):
    """_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    form = CustomAuthenticationForm()
    message = ''
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        message = 'Identifiants invalides.'
    return render(
        request,
        'registration/login.html',
        context={'form': form, 'message': message}
    )
@login_required
def user_dashboard(request):
    """_summary_
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    return render(request, 'dashboard/dashboard.html')