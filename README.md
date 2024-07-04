# Share-it

## Overview
**ShareIt** is a web application designed to facilitate a secure and private file sharing with a built-in expiry mechanism. Users can upload files, generate unique download links, and manage their profiles. The application includes features such as user registration, authentication, file uploads, and the ability to view and manage upload history.

## Technologies Used
### Frontend
- **HTML**: The structure of the web pages.
- **CSS**: Styling of the web pages.
  - **Bootstrap**: Used for responsive design and UI components.
- **JavaScript**: Client-side scripting for dynamic interactions.
  - **jQuery**: Simplifies HTML DOM tree traversal and manipulation.

### Backend
- **Python**: The main programming language for backend development.
  - **Django**: The web framework used to build the application.

## Database
- **PostgreSQL**: For development and production, ensuring scalability and robustness.

## Project Structure
### User Registration and Authentication
- Custom user model extending Django's `AbstractBaseUser` and `PermissionMixin`.
- User registration with email, full name, password, and primary use.
- Custom user manager for creating regular users and superusers.
- JWT authication for secure login and session management.

## File Upload and Management
- `UploadFile` model to handle file uploads.
   - Fields: file, file_name, file_size, upload_date, expiration_date, upload_by, download_link, delete_link
- Unique download links and expiration times for uploaded files.
- Custom file size display and validation using Django template tags.

## User Profile and History
- Custom token generator for secure user identifiers.
- JavaScript validation for user input on frontend forms.
- Custom error handling and messaging using Django's messaging framework

# Getting Started
## Prerequisites
- Python 3.8 and above
- Django 3.2 and above
- PostgreSQL (development and production)

## Installation
1. **Clone the repository**
```
git clone https://github.com/ay0x/Share-it.git
cd Share-it
```

2. **Create and activate a virtual environment**:
```
python -m venv venv
source venv/bin/activate
```

3. **Install the dependencies**:
```
pip install -r requirements.txt
```

4. **Apply the migrations**:
```
python manage.py migrate
```

5. **Create a superuser**:
```
python manage.py createsuperuser
```

6. **Run the development server**:
```
python manage.py runserver
```

## Deployment
- **Configure PostgreSQL**: Ensure your database settings in `settings.py` are configured for PostgreSQL.
- **Collect static files**:
```
python manage.py collectstatic
```
- **Deploy using a WSGI server**: (e.g., Gunicorn) behind a reverse proxy (e.g., Nginx).

# Usage
## Registration
- Users can register by providing their full name, email, password, and primary use.

## Guest User
- Guest user can upload and share files but with limitations e.g. 300 Megabyte file upload limit and no upload history

## File Upload
- Authenticated and guest user can upload files and generate unique download links.

## Profile Management
- Registered users can view and update their profile information.

## Upload History
- Registered users can view their uploaded files and manage them.

# Contributing
Although this is the final portfolio project for ALX Software Engineering Programme, contributions are welcome! Please fork the repository and create a pull request with your changes.
