from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from applications.account.handlers.signin import signinHandler

# todo save tokens in the dbms
TOKENS = {}

def signup(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User with this email already exists.")
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name.split(" ")[0],
                last_name=" ".join(full_name.split(" ")[1:]),
            )
            messages.success(request, "Account created successfully!")
            login(request, user) 
            return redirect("/profile/")
    return render(request, 'signup.html', {"title": "AvantKeel"})

def signin(request):
    response = signinHandler(request)
    if response:
            return response
    return render(request, "signin.html", {"title": "AvantKeel"})


@login_required
def profile(request):
    return render(request, "profile.html", {
        "user": request.user,
        "title": "Profile"
    })


def signout(request):
    logout(request)
    return redirect("/signin/")