![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
# Simple DRF API-project with PyJWT-authorization.
Run on <a href="http://147.45.162.232/api/register">147.45.162.232</a> with Django and Browsable API.<br>
#### API-endpoints:
- /api/register/
- /api/login/
- /api/refresh/
- /api/me/
- /api-doc/<br>


Admin zone: /admin/<br>
Superuser: admin@amin.com<br>
123Qwe123<br>
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
