from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def signinHandler(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/profile/")
        else:
            messages.error(request, "Invalid email or password")

    return None