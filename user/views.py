from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserDetailsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user import views as users

# Create your views here.
def register(request):
    if request.method == 'POST':
        # pass
        form = CreateUserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')

    else:
        form = CreateUserDetailsForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

#logout
def logout(request):
    request.session.clear()
    messages.success(request, ("You were logged out"))
    return render(request, 'user/logout.html', {})


