from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Import render instead of HttpResponse

def homePage(request):
    # This looks into templates/pages/home.html
    return render(request, 'pages/home.html')

def applicationPage(request):
    # If you have an app-specific page, render it here too
    return render(request, 'pages/app.html')

def signUpPage(request):
    return render(request, 'pages/signup.html')

def signInPage(request):
    return render(request, 'pages/signin.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
    path('app/', applicationPage),
    path('signup/',signUpPage),
    path('signin/',signInPage)
]