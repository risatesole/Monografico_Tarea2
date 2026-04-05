"""
This module provides a utility for validating passwords.
It uses Django's internal validation hierarchy to check for:
- Minimum length
- Common passwords (e.g., '123456')
- Similarity to user attributes (email/username)
- Numeric-only passwords
"""

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def is_password_valid(password: str, user=None):
    """
    Validates a password against Django's configured validators.
    Returns True if valid, or a list of error messages if invalid.
    
    Example usage:
    ```
    result = is_password_valid("Qwerty123!")
    
    if result is True:
        print("Password is secure.")
    else:
        print(f"Errors: {', '.join(result)}")
    ```
    """
    try:
        # validate_password checks all validators defined in settings.py
        validate_password(password, user=user)
        return True
    except ValidationError as e:
        # e.messages returns a list of human-readable error strings
        return e.messages
