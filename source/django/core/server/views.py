from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from utils.adapters.httpAdapter import Request , Response
from .handler.hello.HelloHandler import HelloHandler

employees = []

def handleSignup(req: Request, res: Response):
    successResponse = {
        "success": True,
        "message": "Account created successfully",
        "data": {
            "user": {
                "id": "f93dfe6a-0eaf-4c01-ab59-6d6745e6945b",
                "username": "henry",
                "email": "someone@example.com",
                "display_name": "someone",
                "locale": "en-US",
                "timezone": "America/Santo_Domingo",
                "email_verified": False,
                "created_at": "2026-03-14T21:05:22Z"
            },
            "session": {
                "session_id": "sess_7c82fa91",
                "device": {
                    "name": "Henry's Laptop",
                    "type": "desktop"
                },
                "created_at": "2026-03-14T21:05:22Z",
                "tokens": {
                    "access_token": "access_token",
                    "refresh_token": "refresh_token",
                    "expires_in": 3600
                }
            }
        }
    }

    fieldErrorResponse = {
        "success": False,
        "message": "There where an error in one of the fields",
        "error": {
            "type": "CONFLICT",
            "code": "FIELDERROR",
            "fields": {
                "username": {
                    "message": "",
                    "errorcode": "",
                    "haserror": False,                    
                },
                "firstname": {
                    "message": "",
                    "errorcode": "",
                    "haserror": False

                },
                "lastname": {
                    "message": "",
                    "errorcode": "",
                    "haserror": False
                },
                "email": {
                    "message": "",
                    "errorcode": "",
                    "haserror": False
                },
                "password": {
                    "message": "",
                    "errorcode": "",
                    "haserror": False
                },
            }
        }
    }

    res.json( fieldErrorResponse , status=400)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        req = Request(request);
        res = Response()
        try:
            # body = json.loads(request.body)
            answare = handleSignup(req,res)

            return JsonResponse(res.data,status=res.status)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)













@csrf_exempt
def hello_view(request):
    req = Request(request)
    res = Response()
    HelloHandler(req, res)
    return JsonResponse(res.data, status=res.status)


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
