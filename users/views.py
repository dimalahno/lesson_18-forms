from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def home(request):
    return render(request, "users/home.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect("users:home")
            return render(request, "users/registration_success.html", {"username": user.username})

    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})