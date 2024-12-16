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
- PostgreSQL (for production use) or SQLite (for development use)

## Setup Instructions

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd project_management_tool
2. Set Up a Virtual Environment
Create and activate a virtual environment:

bash
Copy code
# On Linux/Mac
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
3. Install Dependencies
Install the required dependencies listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
4. Set Up the Database
The project uses PostgreSQL by default, but SQLite is configured for development. To set up the database:

Create a PostgreSQL database (if using PostgreSQL):

Create a new database using your PostgreSQL client (e.g., pgAdmin).
Update the DATABASES settings in settings.py if you're using a custom database.
Run database migrations to create the necessary tables:

bash
Copy code
python manage.py migrate
5. Create a Superuser (Optional)
If you want to access the Django admin interface, create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the superuser account.

6. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
The project should now be running at http://127.0.0.1:8000.

Accessing the API
The API is accessible via the following URL:

Base URL: http://127.0.0.1:8000/api/
API Documentation
Swagger Documentation: You can view the Swagger UI documentation by navigating to the following URL in your browser:

arduino
Copy code
http://127.0.0.1:8000/swagger/
The Swagger UI will list all available endpoints, request/response formats, and provide an interactive interface to test the API.

Postman Collection: You can also use the Postman collection for API testing. Download the collection file here or import it into your Postman app.

Available Endpoints
1. User Endpoints
POST /api/register/: Register a new user.
POST /api/login/: Login a user.
GET /api/{id}/: Get user details.
PUT /api/{id}/update/: Update user details.
DELETE /api/{id}/delete/: Delete a user account.
2. Project Endpoints
GET /api/projects/: Get the list of projects.
POST /api/projects/: Create a new project.
GET /api/projects/{id}/: Get details of a specific project.
PUT /api/projects/{id}/: Update a project.
DELETE /api/projects/{id}/: Delete a project.
3. Task Endpoints
GET /api/projects/{project_id}/tasks/: List tasks for a project.
POST /api/projects/{project_id}/tasks/: Create a new task.
GET /api/tasks/{id}/: Get task details.
PUT /api/tasks/{id}/: Update a task.
DELETE /api/tasks/{id}/: Delete a task.
4. Comment Endpoints
GET /api/tasks/{task_id}/comments/: List comments for a task.
POST /api/tasks/{task_id}/comments/: Create a comment on a task.
GET /api/comments/{id}/: Get comment details.
PUT /api/comments/{id}/: Update a comment.
DELETE /api/comments/{id}/: Delete a comment.
Testing the API with Postman
You can test the API by using the Postman collection:

Open Postman.
Click on Import and select the downloaded Postman collection file (or use the provided collection link).
Select the desired API endpoint and HTTP method (GET, POST, PUT, DELETE).
Send the request to see the response from the API.
Example Request
Register a New User
POST http://127.0.0.1:8000/api/register/

Request Body:

json
Copy code
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
Response:

json
Copy code
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
Create a New Project
POST http://127.0.0.1:8000/api/projects/

Request Body:

json
Copy code
{
  "name": "Project Alpha",
  "owner": 1
}
Response:

json
Copy code
{
  "id": 1,
  "name": "Project Alpha",
  "owner": 1,
  "created_at": "2024-12-16T12:34:56.789Z"
}
Submitting the Project
Push your code to a Git repository (e.g., GitHub).
Include this README.md file with instructions.
Provide the link to your Git repository and API documentation (Swagger or Postman collection) for submission.
Use the following Google Form to submit your project.
