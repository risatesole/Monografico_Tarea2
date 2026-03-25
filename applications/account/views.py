from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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
            return redirect("/signin/")

    return render(request, 'signup.html', {"title": "AvantKeel"})


def signin(request):
    return render(request, 'signin.html', {"title": "AvantKeel"})