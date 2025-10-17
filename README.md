Food Delivery Application

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [UX Design](#ux-design)
   - [Strategy](#strategy)
   - [Scope](#scope)
   - [Structure](#structure)
   - [Skeleton](#skeleton)
   - [Surface](#surface)
4. [User Stories](#user-stories)
5. [Features](#features)
   - [Implemented Features](#implemented-features)
   - [Future Enhancements](#future-enhancements)
6. [Models](#models)
7. [Views](#views)
8. [URLs](#urls)
9. [Templates](#templates)
10. [Static Files](#static-files)
11. [Testing](#testing)
12. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)
13. [Technologies Used](#technologies-used)
14. [Credits and Acknowledgements](#credits-and-acknowledgements)

Overview

The Food Delivery Application is a Django-based web platform that enables restaurants to register, manage their menus, and maintain their profiles. It is designed to simplify menu management for restaurant owners while providing users with an easy way to view restaurants and their offerings.
The project demonstrates full-stack development using Django’s Model–View–Template (MVT) architecture and standard web development practices. It includes user authentication, form handling, CRUD functionality for menu items, and responsive design through custom CSS.
This application is deployed on Heroku using a Procfile, requirements.txt, and runtime.txt for configuration and environment management.

Project Structure
The application’s structure is as follows (excluding virtual environment files):

food-delivery-app/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── fooddelivery/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── restaurants/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── static/restaurants/css/
│   │   ├── auth-bg.css
│   │   ├── dashboard.css
│   │   ├── login.css
│   │   ├── profile.css
│   │   └── signup.css
│   │
│   └── templates/restaurants/
│       ├── _navbar.html
│       ├── dashboard.html
│       ├── login.html
│       ├── profile.html
│       └── signup.html
│
└── Procfile

UX Design
Strategy
The goal of the application is to provide a centralised platform for restaurants to manage their menus without relying on third-party aggregators. It gives control to restaurant owners while presenting customers with a simple interface to explore restaurant options.
Scope
The application covers the following core functionalities:
* Restaurant registration and authentication.
* Profile creation and editing.
* Menu item management (add, edit, delete).
* Customer-facing templates for viewing restaurants and menu items.
* A clean, responsive user interface styled using custom CSS.
Structure
The project follows Django’s MVT pattern:
* Models define the restaurant and menu item data.
* Views control business logic and page responses.
* Templates render the content displayed to the user.
Navigation includes:
* Signup and login pages.
* A dashboard for restaurant management.
* Profile management page.
* A navbar for navigation consistency across all templates.
Skeleton
Wireframes were designed at the planning stage to define page layout and structure.Insert here: screenshots or diagrams of wireframes.
Surface
A simple, minimalist design with consistent colours and clear typography was implemented. CSS files are modular, ensuring maintainable styling across login, signup, dashboard, and profile pages.

User Stories
1. As a restaurant owner, I want to create an account so that I can manage my restaurant information.
2. As a restaurant owner, I want to add, edit, or delete menu items so that I can keep my restaurant offerings up to date.
3. As a customer, I want to view restaurants and their menus so that I can decide where to order from.
4. As a user, I want to log in securely and manage my profile.
5. As a system administrator, I want to ensure that only authenticated users can manage menus.
Each user story has been implemented and validated through manual testing.

Features
Implemented Features
User Authentication
* Django’s built-in user model is extended through forms for registration and login.
* Custom login and signup templates.
Restaurant Management
* Each restaurant owner can manage their own menu items through a dashboard interface.
* Profile management is available through dedicated views and templates.
Forms
* Forms for user signup, login, profile editing, and menu item management are defined in forms.py.
Templates
* Templates are located within restaurants/templates/restaurants/.
* They include a shared _navbar.html for navigation consistency.
Static Files
* Custom CSS for each key view, located under restaurants/static/restaurants/css/.
Database
* SQLite3 database used for development.
* Models define restaurants, menu items, and related attributes.
Future Enhancements
Insert here:Future plans may include:
* Integration of online ordering and checkout functionality.
* API endpoints for mobile integration.
* Customer reviews and ratings.
* Payment processing using Stripe or PayPal.

Models
Located in restaurants/models.py, the models define database structure for restaurants and their menu items.Example summary:
* Restaurant: stores name, owner, and profile information.
* MenuItem: linked to the restaurant model via a foreign key, storing name, price, and description.

Views
Located in restaurants/views.py.The views handle:
* User registration and authentication.
* Dashboard rendering and CRUD actions for menu items.
* Profile display and updates.
Views use Django’s built-in decorators for authentication and standard view functions for rendering templates and handling forms.

URLs
The restaurants/urls.py file defines routes for each page including:
* /login/
* /signup/
* /dashboard/
* /profile/
The project-level fooddelivery/urls.py routes traffic to the restaurant app.

Templates
The templates under restaurants/templates/restaurants/ include:
* login.html – login form.
* signup.html – new user registration.
* dashboard.html – menu management dashboard.
* profile.html – profile details and edit form.
* _navbar.html – reusable navigation component.
Each template inherits consistent structure and references the appropriate CSS files from the static directory.

Static Files
Static assets are located in restaurants/static/restaurants/css/, providing a modular styling approach:
* auth-bg.css – background styling for authentication pages.
* login.css and signup.css – form and input design.
* dashboard.css – grid layout for menu and restaurant management.
* profile.css – styling for the profile management interface.

Testing
Manual testing was conducted for all major functionalities.

Test Scenarios

| Test               | Expected Result                             | Outcome |
| ------------------ | ------------------------------------------- | ------- |
| User registration  | New user created and redirected to login    | Pass    |
| User login         | Redirects to dashboard after authentication | Pass    |
| Menu item creation | Item saved and displayed on dashboard       | Pass    |
| Menu item deletion | Item removed from list                      | Pass    |
| Profile update     | Information updated successfully            | Pass    |
| Template rendering | All templates load correctly without errors | Pass    |
| CSS linkage        | Static files applied consistently           | Pass    |


Validation
* HTML/CSS validated through W3C Validator.
* Python validated with python manage.py check.
* All migrations applied successfully with python manage.py migrate.
Insert here: screenshots or links to validation reports.

Deployment
Heroku Deployment
1. Ensure all dependencies are listed in requirements.txt.
2. Create a Procfile with the following content:web: gunicorn fooddelivery.wsgi
3. 
4. Commit changes:git add .
5. git commit -m "Prepare for Heroku deployment"
6. 
7. Login to Heroku:heroku login
8. 
9. Create the app:heroku create your-app-name
10. 
11. Push code to Heroku:git push heroku main
12. 
13. Run migrations:heroku run python manage.py migrate
14. 
15. Open the deployed application:heroku open
16. 
The application runs in production mode using Gunicorn as the WSGI HTTP server.
Local Deployment
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies with pip install -r requirements.txt.
4. Run python manage.py migrate.
5. Start the local server with python manage.py runserver.
6. Visit http://127.0.0.1:8000/.

Technologies Used
* Python 3.12 – Core programming language.
* Django 5.2.7 – Framework for rapid web development.
* SQLite3 – Database engine used for development.
* HTML5 / CSS3 – Front-end structure and styling.
* Heroku – Cloud hosting platform for deployment.
* Gunicorn – WSGI server used in production.
* Git & GitHub – Version control and repository hosting.
* Visual Studio Code – IDE used during development.
AI Tools Used
GitHub Copilot and ChatGPT were used for limited assistance with code suggestions and documentation drafting. All code and documentation were manually reviewed, edited, and verified to ensure originality and accuracy.

Credits and Acknowledgements
Code References
* Django official documentation (https://docs.djangoproject.com) for setup and model guidance.
* Tutorials on Django authentication and CRUD operations for structural inspiration.
Media and Content
All templates, CSS, and textual content created by the developer.
Acknowledgements
* Code Institute for providing project structure and assessment standards.
* GitHub Copilot and ChatGPT for AI-assisted code suggestions and documentation support.







