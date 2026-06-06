# DataEntry Application - Installation Guide

Complete step-by-step guide to install and run the DataEntry application.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Starting the Server](#starting-the-server)
4. [First Time Setup](#first-time-setup)
5. [Troubleshooting](#troubleshooting)

---

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.8 or higher
- **RAM**: 1GB minimum
- **Disk Space**: 500MB minimum

### Verify Python Installation

```bash
python --version
```

If Python is not installed, download from [python.org](https://www.python.org/downloads/)

---

## Installation Steps

### Step 1: Navigate to Project Directory

**Windows (Command Prompt or PowerShell):**
```bash
cd ../projectfolder
```

**macOS/Linux:**
```bash
cd /path/to/websitewithpythondjango
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Or install individually:**
```bash
pip install Django==5.2.13
pip install Pillow==11.2.0
```

### Step 3: Verify Installation

```bash
python manage.py check
```

You should see: `System check identified no issues (0 silenced).`

### Step 4: Database Setup (Already Done)

If you're setting up fresh:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

---

## Starting the Server

### Quick Method: Use Setup Script

**Windows:**
```bash
setup.bat
```

**macOS/Linux:**
```bash
bash setup.sh
```

This will guide you through creating an admin account and start the server.

### Manual Method: Step-by-Step

#### Step 1: Create Admin Account

```bash
python manage.py createsuperuser
```

You'll be prompted for:
- **Username**: Enter username for admin account (e.g., `admin`)
- **Email**: Enter email address (e.g., `admin@example.com`)
- **Password**: Enter a secure password
- **Password (again)**: Confirm the password

Example:
```
Username: admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

#### Step 2: Run Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Access the Application

Open your web browser and navigate to:

| URL | Purpose |
|-----|---------|
| http://localhost:8000/login/ | User login page |
| http://localhost:8000/signup/ | User registration page |
| http://localhost:8000/admin/ | Django admin panel |

**Admin Panel Login**: Use the superuser credentials you just created

---

## First Time Setup

### 1. Create Your First Admin User

While the server is running, visit: `http://localhost:8000/admin/`

Login with superuser credentials created earlier.

### 2. Explore Admin Interface

- Navigate to "User Profiles" to manage users
- Navigate to "Entities" to view/manage data entries

### 3. Create Test Users

**Via Admin Panel:**
1. Go to "Users" section
2. Click "Add User"
3. Enter username and password
4. Click "Save"

**Via Application:**
1. Go to `http://localhost:8000/signup/`
2. Fill in the registration form:
   - Full Name
   - Username
   - Email
   - Password (and confirm)
   - Avatar (optional)
3. Click "Create Account"

### 4. Test the Application

1. **Sign Up**: Create a new account via signup page
2. **Login**: Login with your credentials
3. **Add Entries**: Add some data entries from the home page
4. **View Profile**: Click on your avatar dropdown
5. **Edit Profile**: Update your profile information
6. **Logout**: Test logout functionality

---

## Troubleshooting

### Issue: "Port 8000 already in use"

**Solution:** Use a different port
```bash
python manage.py runserver 8001
```

### Issue: "No module named 'django'"

**Solution:** Install Django
```bash
pip install Django
```

### Issue: Database error "no such table"

**Solution:** Run migrations
```bash
python manage.py migrate
```

### Issue: Static files (CSS) not loading

**Solution 1:** Clear browser cache (Ctrl+F5)

**Solution 2:** Collect static files
```bash
python manage.py collectstatic --noinput
```

### Issue: Avatar upload doesn't work

**Verification:**
1. Check if `media` folder exists in project root
2. Verify folder has write permissions
3. Ensure DEBUG=True in settings.py (for development)

**Solution:** Create media folder if missing
```bash
mkdir media
mkdir media/avatars
```

### Issue: "SyntaxError" in Python code

**Solution:** Verify Python version
```bash
python --version
```
Must be Python 3.8 or higher

### Issue: "CSRF verification failed"

**Solution:** 
1. Clear browser cookies
2. Restart development server
3. Try again in a different browser/incognito window

---

## Project Structure After Setup

```
websitewithpythondjango/
├── db.sqlite3                 # Database (created after migrate)
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── setup.bat / setup.sh       # Setup scripts
├── README.md                  # Project README
├── INSTALLATION_GUIDE.md      # This file
├── DataEntryProject/          # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── DataEntry/                 # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── signals.py
│   ├── apps.py
│   ├── migrations/            # Database versions
│   └── __pycache__/
├── templates/                 # HTML templates
│   ├── base.html
│   └── DataEntry/
│       ├── login.html
│       ├── signup.html
│       ├── home.html
│       ├── profile.html
│       ├── profile_edit.html
│       ├── change_password.html
│       ├── entity_detail.html
│       └── entity_confirm_delete.html
├── static/                    # CSS, JS, images
│   └── css/
│       └── style.css
└── media/                     # User uploads
    └── avatars/               # User profile pictures
```

---

## Next Steps

After successful installation:

1. **Explore the Admin Panel**: `http://localhost:8000/admin/`
2. **Create Test Data**: Add users and data entries
3. **Customize Settings**: Modify `DataEntryProject/settings.py` as needed
4. **Understand File Structure**: Review models, views, and forms
5. **Customize Templates**: Modify HTML templates in the `templates/` directory
6. **Customize Styling**: Edit CSS in `static/css/style.css`

---

## Common Tasks

### Add a New Data Entry Field

1. Edit `DataEntry/models.py` - Entity model
2. Add new field: `new_field = models.CharField(max_length=255)`
3. Create migration: `python manage.py makemigrations`
4. Apply migration: `python manage.py migrate`
5. Update form in `DataEntry/forms.py`
6. Update template: `templates/DataEntry/home.html`

### Change Application Name

1. Database: Rename models or create new ones
2. URL namespace: Update URL patterns
3. Templates: Update references
4. Static files: Organize by app name

### Deploy to Production

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Generate new `SECRET_KEY`
4. Use production database (PostgreSQL recommended)
5. Use a production web server (Gunicorn, uWSGI)
6. Configure static file serving (WhiteNoise, nginx)
7. Set up HTTPS/SSL certificate

---

## Getting Help

### Documentation
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Pillow Image Library](https://pillow.readthedocs.io/)

### Common Django Commands
```bash
# Create new app
python manage.py startapp app_name

# List available commands
python manage.py help

# Run Django shell
python manage.py shell

# Create database backup
python manage.py dumpdata > backup.json

# Load database backup
python manage.py loaddata backup.json

# Run tests
python manage.py test
```

---

**Last Updated**: April 2026
**Version**: 1.0.0
