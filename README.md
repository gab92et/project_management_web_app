# project_management_web_app

Overview
The Project Management Django App is a web application built using Django framework that helps manage projects, tasks, and workers within an organization. It provides features for project managers to create projects, assign tasks to workers, track task advancements, and monitor project progress.

Features
Project Management: Project managers can create new projects, view project details, and assign tasks to workers.
Task Assignment: Project managers can assign tasks to specific workers within a project.
Task Advancement: Workers can update the advancement percentage of tasks assigned to them.
Project Progress Tracking: Project managers can track the progress of projects by viewing the average advancement of all tasks within a project.


How to Use
Installation:
Clone the repository: git clone <repository-url>
Install dependencies: pip install -r requirements.txt
Database Setup:
Run migrations: python manage.py migrate
Create Superuser (Optional):
Create a superuser to access the Django admin interface: python manage.py createsuperuser
Run the Server:
Start the development server: python manage.py runserver
Access the Application:
Open a web browser and go to http://localhost:8000/ to access the application.
Login with the superuser credentials or create a new account to access the project management features.

Project Management:
Create a new project by clicking on the "Create Project" button.
Assign tasks to workers by selecting a project and clicking on the "Assign Task" button.
View project details and track progress by clicking on a project title.
Update task advancements by clicking on the "Update" button next to each task in the project detail view.
Search for specific projects or workers using the search bar.

Technologies Used
Django: Python-based web framework for building web applications.
HTML: Markup language for creating web pages.
CSS: Stylesheet language for styling web pages.
SQLite: Database management system used for storing project and task data.
License
This project is licensed under the MIT License - see the LICENSE file for details.
