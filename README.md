# Campus Skill Swap

A Django-based marketplace platform for students to post and book skills or services with each other.

## Overview

Campus Skill Swap is a community-driven skill-sharing platform that enables students to offer services (tutoring, design, programming, writing, and more) to their peers. Users can create skill listings, browse available services, leave reviews, and request bookings for sessions.

### Key Features

- **User Authentication**: Register, login, and manage user accounts
- **Skill Listings**: Create, edit, and delete skill/service posts with flexible pricing options (free or paid)
- **Marketplace Search**: Browse all available skills and search by title or category
- **Booking System**: Request sessions from skill providers with optional dates and messages
- **Reviews & Ratings**: Leave feedback and ratings on completed or in-progress services
- **User Dashboard**: View your posted skills, sent booking requests, and received booking requests
- **Availability Management**: Set your skill's availability status (Available, Busy, Closed)
- **Contact Preferences**: Specify preferred contact method (Email, Phone, In-App Message)

## Tech Stack

- **Backend**: Django 6.0.4
- **Database**: SQLite (configurable in settings)
- **Additional Libraries**:
  - asgiref==3.11.1
  - sqlparse==0.5.5
  - tzdata==2026.1

## Setup Instructions

### 1. Activate the Virtual Environment

**PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Apply Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser (Optional)

To access the Django admin interface:
```powershell
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/` with your credentials.

### 5. Run the Development Server

```powershell
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
campus_skillswap/
├── campus_skillswap/      # Django project configuration
│   ├── __init__.py
│   ├── asgi.py           # ASGI configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL routing
│   └── wsgi.py           # WSGI configuration
├── MainApp/              # Main application
│   ├── models.py         # Database models (Skill, Review, BookingRequest)
│   ├── views.py          # Request handlers
│   ├── forms.py          # Form definitions
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Django admin configuration
│   ├── tests.py          # Unit tests
│   ├── migrations/       # Database migration files
│   └── templates/        # HTML templates
│       └── MainApp/
│           ├── base.html
│           ├── home.html
│           ├── login.html
│           ├── register.html
│           ├── dashboard.html
│           ├── skill_form.html
│           ├── skill_detail.html
│           └── skill_confirm_delete.html
├── static/               # Static assets
│   └── css/
│       └── styles.css
├── manage.py             # Django management utility
├── db.sqlite3            # SQLite database file
└── requirements.txt      # Python dependencies
```

## Database Models

### Skill
Represents a skill or service offered by a user.

**Fields:**
- `title` - Name of the skill (max 120 characters)
- `description` - Detailed description
- `category` - Type of skill (Tutoring, Design, Programming, Writing, Other)
- `price` - Cost (optional; use with `is_free`)
- `is_free` - Boolean flag to mark skill as free
- `contact_preference` - Preferred contact method (Email, Phone, In-App Message)
- `availability_status` - Current availability (Available, Busy, Closed)
- `created_at` - Timestamp of creation
- `owner` - Foreign key to the User who posted the skill

### Review
Stores user reviews and ratings for skills.

**Fields:**
- `skill` - Foreign key to the reviewed Skill
- `reviewer` - Foreign key to the User leaving the review
- `rating` - Numeric rating
- `comment` - Optional review text
- `created_at` - Timestamp of creation

### BookingRequest
Tracks booking/session requests for skills.

**Fields:**
- `skill` - Foreign key to the requested Skill
- `requester` - Foreign key to the User requesting the session
- `message` - Optional message from requester
- `requested_date` - Proposed date for the session (optional)
- `status` - Request status (Pending, Approved, Declined)
- `created_at` - Timestamp of creation

## Main Views/Pages

- **Home** (`/`) - Marketplace with all available skills and search functionality
- **Register** (`/register/`) - User registration
- **Login** (`/login/`) - User login
- **Logout** (`/logout/`) - User logout
- **Dashboard** (`/dashboard/`) - User's personal hub for skills and booking requests
- **Skill Detail** (`/skill/<id>/`) - View skill details, reviews, and make booking requests
- **Create Skill** (`/create-skill/`) - Post a new skill listing
- **Edit Skill** (`/skill/<id>/edit/`) - Update an existing skill
- **Delete Skill** (`/skill/<id>/delete/`) - Remove a skill listing

## Usage Tips

1. **Creating a Skill**: Log in, navigate to your dashboard, and click "Create a Skill Post" to list a service
2. **Finding Skills**: Use the search bar on the home page to find skills by name or category
3. **Booking a Service**: Click on a skill to see details, then fill out the booking form with your message and preferred date
4. **Leaving Reviews**: After using a service, you can rate and review it on the skill detail page
5. **Managing Requests**: Check your dashboard to view and manage incoming booking requests

## Notes

- The project uses SQLite for the database, suitable for development and small deployments
- Django is installed in a virtual environment (`.venv`) to isolate dependencies
- All timestamps use the timezone configured in Django settings
- User authentication uses Django's built-in user model and authentication system
