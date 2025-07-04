from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            selected_type = form.cleaned_data['user_type']

            user = authenticate(request, username=username, password=password)
            if user:
                profile = user.userprofile
                if profile.user_type != selected_type:
                    form.add_error(None, 'Incorrect role selected for this account.')
                else:
                    login(request, user)
                    if profile.user_type == 'admin':
                        return redirect('/adminpanel/confirmed-bookings/')
                    elif profile.user_type == 'manager':
                        return redirect('/testcentre/manage/')
                    else:
                        return redirect('/booking/')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')

