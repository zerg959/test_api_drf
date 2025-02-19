# user-api
### Simple API-project.
Run on 147.45.162.232 with Django and Browsable API.<br>
API-points:
- /api/register/
- /api/login/
- /api/refresh/
- /api/me/
- /api-doc/
Admin zone:<br>
/admin/<br>
Superuser: admin@amin.com 123Qwe123<br>
<br>
================================ Description =========================<br>
- REST API for a user authentication and authorization system using Django and Django REST Framework.<br>
- The system supports user registration, authentication, token refresh, logout, and allow users to retrieve and update their personal information.<br>
- Authentication utilizes Access and Refresh tokens.<br>
- Refresh Token – A UUID stored in the database, issued for 30 days by default.<br>
- Access Token – A JSON Web Token with a default lifespan of 30 seconds.<br>
- Used the django-constance module for managing the lifetimes of Access and Refresh tokens.<br>
- Superuser can manage with lifetime parameters of tokens in admin area (ip/admin).<br>
- Clients may request an Access Token refresh at any time, for instance, upon Access Token expiry by providing a valid Refresh Token.<br>
- In this case, the service returns a new valid pair of Access and Refresh Tokens, resetting their lifespans.<br>
- Provide a browsable API with endpoint documentation.<br>
--------------
