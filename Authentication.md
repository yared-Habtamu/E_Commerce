Authentication Documentation

Overview
This document provides details on how authentication is implemented in the E-commerce API, including how to test it using tools like Postman. The authentication setup ensures that certain endpoints are secure and accessible only to authorized users.

Authentication Implementation

1. Authentication Method
We have implemented token-based authentication using Django Rest Framework (DRF):
- TokenAuthentication: Each user is assigned a token upon login. This token must be included in the Authorization header for secured API requests.

2. Steps to Enable Authentication
- Installed djangorestframework and djangorestframework-simplejwt for JWT token-based authentication.
- Added rest_framework and rest_framework_simplejwt to the INSTALLED_APPS in settings.py.
- Configured DEFAULT_AUTHENTICATION_CLASSES in settings.py:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

- Created endpoints for login (/api/token/) and refreshing tokens (/api/token/refresh/).
- Secured endpoints by applying the @permission_classes([IsAuthenticated]) decorator to views requiring authentication.

How to Test Authentication

1. Obtain a Token
- Endpoint: /api/token/
- Method: POST
- Request Body:

```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

- Response:

```json
{
    "access": "<JWT_ACCESS_TOKEN>",
    "refresh": "<JWT_REFRESH_TOKEN>"
}
```

Save the access token as it will be used for subsequent requests.

2. Access Secured Endpoints
- Include the Authorization header with the token:

```
Authorization: Bearer <JWT_ACCESS_TOKEN>
```

- Example with Postman:
  1. Open Postman.
  2. Select the request type (e.g., GET or POST).
  3. Enter the secured endpoint URL (e.g., http://127.0.0.1:8000/api/products/).
  4. Go to the Authorization tab, set the type to Bearer Token, and paste the access token.
  5. Send the request.

3. Refresh the Token
- Endpoint: /api/token/refresh/
- Method: POST
- Request Body:

```json
{
    "refresh": "<JWT_REFRESH_TOKEN>"
}
```

- Response:

```json
{
    "access": "<NEW_JWT_ACCESS_TOKEN>"
}
```

Use the new access token for subsequent requests.

Example Credentials for Testing
- Username: iamzuser
- Password: mypassword


