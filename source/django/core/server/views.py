from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

employees = []


def hello_view(request):
    return JsonResponse({
        "message": "Hello, world!"
    })


def createEmployee(body):
    client_data = {
        "id": len(employees) + 1,
        "first_name": body.get("first_name"),
        "last_name": body.get("last_name"),
        "email": body.get("email"),
        "role": body.get("role"),
    }

    employees.append(client_data)
    return client_data


def viewEmployee():
    return employees


def deleteEmployee(emp_id):
    global employees

    for emp in employees:
        if emp["id"] == emp_id:
            employees = [e for e in employees if e["id"] != emp_id]
            return True

    return False  # if not found


@csrf_exempt
def employee(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            new_employee = createEmployee(body)

            return JsonResponse({
                "message": "Employee created successfully",
                "employee": new_employee
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    elif request.method == "GET":
        return JsonResponse({
            "employees": viewEmployee()
        })

    elif request.method == "DELETE":
        emp_id = request.GET.get("id")

        if not emp_id:
            return JsonResponse({
                "error": "Employee id is required"
            }, status=400)

        try:
            emp_id = int(emp_id)
        except ValueError:
            return JsonResponse({
                "error": "Invalid id format"
            }, status=400)

        deleted = deleteEmployee(emp_id)

        if not deleted:
            return JsonResponse({
                "error": "Employee not found"
            }, status=404)

        return JsonResponse({
            "message": f"Employee {emp_id} deleted successfully"
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)