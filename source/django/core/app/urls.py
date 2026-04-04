# app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from applications.core.views import home
from applications.employeemanager.views import employeemanager
from applications.core.views import hello_world
from server.views import hello_view

def applicationPage(request):
    return render(request, 'pages/app.html')

urlpatterns = [
    # api routes
    path('api/hello', hello_world), 

    # django admin panel
    path('admin/', admin.site.urls),

    # frontend pages

    # home page
    path('', home),
    # path('app/', employeemanager),
    
    # custom signin, signout and signup endpoints that use django api
    path('', include('applications.account.urls')),  # handles signup/signin
  
    # tarea 1 monografico
    path("app/", include("applications.employeemanager.urls")),
    
    path('api/', include('server.urls')),

]