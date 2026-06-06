# DataEntry Application - Developer Quick Reference

Quick reference guide for common development tasks.

## Quick Start

```bash
# Navigate to project
cd e:\WORK\websitewithpythondjango

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## File Structure at a Glance

| File/Folder | Purpose |
|---|---|
| `manage.py` | Django management commands |
| `settings.py` | Project configuration |
| `urls.py` | URL routing |
| `DataEntry/models.py` | Database models |
| `DataEntry/views.py` | View logic |
| `DataEntry/forms.py` | Form definitions |
| `templates/` | HTML templates |
| `static/css/` | Stylesheets |
| `media/` | User uploads |
| `db.sqlite3` | SQLite database |

## Key Models

### UserProfile
```python
user = OneToOneField(User)  # Links to Django User model
full_name = CharField(max_length=255)
avatar = ImageField()
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

### Entity
```python
user = ForeignKey(User)  # Data owner
title = CharField(max_length=255)
description = TextField()
created_at = DateTimeField(auto_now_add=True)
updated_at = DateTimeField(auto_now=True)
```

## URL Patterns

```python
/login/                      # Login page
/signup/                     # Registration
/logout/                     # Logout
/                            # Home/Dashboard
/profile/                    # View profile
/profile/edit/               # Edit profile
/profile/change-password/    # Change password
/entity/<id>/                # View entry
/entity/<id>/delete/         # Delete entry
/admin/                      # Admin panel
```

## Views at a Glance

| View | Purpose | Auth Required |
|---|---|---|
| `signup_view` | User registration | No |
| `login_view` | User login | No |
| `logout_view` | User logout | Yes |
| `home_view` | Dashboard/Data entry | Yes |
| `profile_view` | View profile | Yes |
| `profile_edit_view` | Edit profile | Yes |
| `change_password_view` | Change password | Yes |
| `entity_detail_view` | View entry details | Yes |
| `entity_delete_view` | Delete entry | Yes |

## Forms Available

- `SignUpForm` - User registration with avatar
- `LoginForm` - Username/email + password login
- `EntityForm` - Create/edit data entries
- `UserProfileForm` - Edit user profile
- `PasswordChangeForm` - Change password

## Common Django Commands

```bash
# Create new app
python manage.py startapp app_name

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run tests
python manage.py test

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Database dump
python manage.py dumpdata > data.json

# Database load
python manage.py loaddata data.json

# Show SQL queries
python manage.py sqlmigrate app_name migration_number

# Check project configuration
python manage.py check
```

## Template Tags Used

```django
{% load static %}                   # Load static files
{% url 'name' %}                   # Reverse URL
{% if condition %}...{% endif %}   # Conditionals
{% for item in items %}...{% endfor %}  # Loops
{{ variable }}                      # Display variable
{{ user.is_authenticated }}        # Check if logged in
{% csrf_token %}                   # CSRF protection
```

## Settings Configuration

```python
# Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
AUTH_PASSWORD_VALIDATORS = [...]

# Media files (uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DataEntry',
]
```

## Common Modifications

### Add a Model Field
1. Edit `DataEntry/models.py`
2. Add the field to the model
3. Create migration: `python manage.py makemigrations`
4. Apply migration: `python manage.py migrate`
5. Update form and template as needed

### Change Login Flow
- Edit `DataEntry/views.py` → `login_view()`
- Modify `DataEntry/forms.py` → `LoginForm`
- Update `templates/DataEntry/login.html`

### Customize Theme
- Edit `static/css/style.css`
- Modify CSS variables in `:root`
- Update color values as needed

### Add Email Verification
1. Install: `pip install django-allauth`
2. Configure settings.py
3. Add email backend settings
4. Update signup flow
5. Create verification template

## Debugging Tips

```bash
# Enable Django debug toolbar
pip install django-debug-toolbar

# Access Django shell
python manage.py shell

# Test views in shell
from DataEntry.models import Entity
Entity.objects.all()
```

## Database Queries in Python

```python
# Import models
from DataEntry.models import Entity, UserProfile
from django.contrib.auth.models import User

# Get all entities
Entity.objects.all()

# Filter by user
Entity.objects.filter(user=request.user)

# Get specific entity
Entity.objects.get(id=1)

# Count entities
Entity.objects.filter(user=request.user).count()

# Delete entity
entity.delete()

# Update entity
entity.title = "New Title"
entity.save()

# Create new entity
Entity.objects.create(user=request.user, title="Title", description="Desc")
```

## CSS Variables

```css
--primary-color: #6366f1         /* Main brand color */
--primary-hover: #4f46e5         /* Hover state */
--secondary-color: #64748b       /* Secondary color */
--danger-color: #ef4444          /* Error/Delete color */
--dark-bg: #0f172a               /* Main background */
--card-bg: #1e293b               /* Card background */
--text-primary: #f1f5f9          /* Main text */
--text-secondary: #cbd5e1        /* Secondary text */
```

## Testing Checklist

- [ ] Signup creates account and profile
- [ ] Login accepts username or email
- [ ] Session persists across pages
- [ ] Avatar uploads and displays
- [ ] Data entry form saves correctly
- [ ] Entries display in user list
- [ ] Profile editing updates data
- [ ] Password change works
- [ ] Logout clears session
- [ ] Admin interface accessible
- [ ] Admin can manage users/entries
- [ ] Forms validate correctly
- [ ] CSS loads and displays properly
- [ ] Mobile view is responsive
- [ ] Redirects work correctly

## Useful Links

- Django Utilities: https://docs.djangoproject.com/
- Form Reference: https://docs.djangoproject.com/en/stable/ref/forms/
- Model Field Types: https://docs.djangoproject.com/en/stable/ref/models/fields/
- Built-in Template Tags: https://docs.djangoproject.com/en/stable/ref/templates/

---

**Quick Reference Version**: 1.0.0
