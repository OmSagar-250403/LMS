LMS Django Application

This README file provides instructions for setting up and running the LMS Django application. The application contains a single app called "home" and provides endpoints for managing applications.

Prerequisites

Ensure the following are installed on your system:

Python (3.8 or higher recommended)

Django (4.0 or higher)

pip (Python package manager)

A virtual environment tool (e.g., venv or virtualenv)

A database (SQLite is used by default, but you can configure others like PostgreSQL or MySQL)

Setup Instructions

Follow these steps to set up and run the application:

1. Clone the Repository

Clone the repository containing the LMS application to your local system:

git clone <repository-url>
cd lms

2. Create and Activate a Virtual Environment

Create a virtual environment to isolate dependencies:

python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate   # For Windows

3. Install Dependencies

Install the required Python packages using the requirements.txt file:

pip install -r requirements.txt

If the requirements.txt file does not exist, manually install Django:

pip install django

4. Configure the Application

Update the Django settings file (settings.py) in the lms directory:

Database Configuration:
By default, SQLite is used. If using another database, update the DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change this if using another DB
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Secret Key:
Ensure the SECRET_KEY in settings.py is set to a secure value.

Allowed Hosts:
Update the ALLOWED_HOSTS list with your domain or IP address:

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

5. Run Database Migrations

Apply the database migrations to set up the necessary tables:

python manage.py migrate

6. Run the Development Server

Start the Django development server:

python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.

Application Endpoints

The LMS application contains the following endpoints, managed by the home app:

Add App

URL: /add-app

Method: POST

Description: Adds a new application.

Get App

URL: /get-app/

Method: GET

Description: Retrieves application details using query parameters.

Delete App

URL: /delete-app/<int:id>

Method: DELETE

Description: Deletes an application by its ID.

App Management

URL: /

Method: GET

Description: Displays the application management interface.

Directory Structure

├── lms/
│   ├── lms/         # Project settings and configurations
│   ├── home/        # Home app containing views, models, and templates
│   ├── manage.py    # Django management script

Additional Notes

Static Files:
Collect static files before deploying:

python manage.py collectstatic

Admin Interface:
Create a superuser to access the Django admin panel:

python manage.py createsuperuser

Access the admin panel at http://127.0.0.1:8000/admin/.

Testing:
Run tests to ensure the application works as expected:

python manage.py test

Deployment

For deployment, consider using production-grade servers like Gunicorn with Nginx and configure your database for production use. Update DEBUG to False in settings.py and ensure proper security configurations.