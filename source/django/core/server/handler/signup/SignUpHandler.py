from utils.adapters.httpAdapter import Request, Response
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from ...models import User

# todo: inteimplement utils/validators

def handleSignup(req: Request, res: Response):
    try:
        # 1. Basic validation (ensure keys exist)
        data = req.body
        required_fields = ["username", "email", "firstname", "lastname", "password"]
        if not all(k in data for k in required_fields):
            res.json({"success": False, "message": "Missing fields"}, status=400)
            return

        # 2. Create user and HASH the password
        new_user = User(
            username=data["username"],
            email=data["email"],
            firstname=data["firstname"],
            lastname=data["lastname"],
            # make_password handles the PBKDF2 hashing for you
            passwordhash=make_password(data["password"]) 
        )
        
        new_user.save()

        # 3. Build response from the ACTUAL saved object
        myResponse = {
            "success": True,
            "message": "Account created successfully",
            "data": {
                "user": {
                    "id": new_user.id,
                    "username": new_user.username,
                    "email": new_user.email,
                }
            }
        }
        res.json(myResponse, status=201)

    except IntegrityError:
        # This catches duplicate usernames/emails based on your model constraints
        res.json({
            "success": False, 
            "message": "Username or Email already exists"
        }, status=409)
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        res.json({
            "success": False, 
            "message": "An internal error occurred"
        }, status=500)




    