# Project Management Tool

This is a project management tool built with Django, Django REST Framework (DRF), and PostgreSQL. It includes features for user authentication, project management, task management, and comments. The API is well-documented and can be accessed via Swagger or Postman.

## Features

- User registration, login, and profile management
- Create, update, and delete projects
- Manage tasks within projects
- Add, update, and delete comments on tasks
- API documentation using Swagger

## Requirements

Before setting up the project, make sure you have the following installed:

- Python 3.10+
- pip (Python package manager)
  SQLite (for development use)

## Setup Instructions

### 1. Clone the Repository

Clone the project repository to your local machine:


git clone <repository-url>
cd project_management_tool
2. Set Up a Virtual Environment
Create and activate a virtual environment:

Copy code
# On Linux/Mac
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
3. Install Dependencies
Install the required dependencies listed in the requirements.txt file:

Copy code
pip install -r requirements.txt
4. Set Up the Database
The project uses by default, but SQLite is configured for development. To set up the database:
 

Copy code
python manage.py migrate
5. Create a Superuser (Optional)
If you want to access the Django admin interface, create a superuser:

Copy code
python manage.py createsuperuser
Follow the prompts to set up the superuser account.

6. Run the Development Server
Start the Django development server:

Copy code
python manage.py runserver
The project should now be running at http://127.0.0.1:8000.

Accessing the API
The API is accessible via the following URL:

Base URL: http://127.0.0.1:8000
API Documentation
Swagger Documentation: You can view the Swagger UI documentation by navigating to the following URL in your browser:

arduino
Copy code
http://127.0.0.1:8000/swagger/
The Swagger UI will list all available endpoints, request/response formats, and provide an interactive interface to test the API.

Postman Collection: You can also use the Postman collection for API testing. Download the collection file here or import it into your Postman app.

Available Endpoints
Here are all the API endpoints:

Comments Endpoints
GET /api/comments/{id}/
DELETE /api/comments/{id}/delete/
PUT /api/comments/{id}/update/
PATCH /api/comments/{id}/update/
Project Endpoints
GET /api/projects/
POST /api/projects/
POST /api/projects/create/
GET /api/projects/{id}/
DELETE /api/projects/{id}/delete/
PUT /api/projects/{id}/update/
PATCH /api/projects/{id}/update/
Task Endpoints
GET /api/projects/{project_id}/tasks/
POST /api/projects/{project_id}/tasks/
POST /api/projects/{project_id}/tasks/create/
GET /api/tasks/{id}/
DELETE /api/tasks/{id}/delete/
PUT /api/tasks/{id}/update/
PATCH /api/tasks/{id}/update/
GET /api/tasks/{task_id}/comments/
POST /api/tasks/{task_id}/comments/
POST /api/tasks/{task_id}/comments/create/
User Endpoints
POST /api/users/login/
POST /api/users/register/
GET /api/users/{id}/
DELETE /api/users/{id}/delete/
PUT /api/users/{id}/update/
PATCH /api/users/{id}/update/
You can test the API by using the Postman collection:

Open Postman.
Click on Import and select the downloaded Postman collection file (or use the provided collection link).
Select the desired API endpoint and HTTP method (GET, POST, PUT, DELETE).
Send the request to see the response from the API.
 
