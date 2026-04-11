from applications.employeemanager.server.handlers.employeeHandler import employeeHandler
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from .models import Employee

@login_required
def employeemanager(request):
    if request.method == "POST":
        Employee.objects.create(
            firstname=request.POST.get("fname"),
            lastname=request.POST.get("lname"),
            role=request.POST.get("role"),
            email=request.POST.get("email"),
            submitted_by=request.user
        )

    employees = Employee.objects.filter(submitted_by=request.user)

    return render(request, "employeemanager/employeemanager.html", {
    # return render(request, "employeemanager/team-todo.html", {
        "title": "AvantKeel",
        "employees": employees
    })
