# DataEntry Application - Django Web Application

A modern, dark-themed Django web application for user management and data entry. Features include user authentication (signup/login), profile management, and a data entry system with entity management.

## Features

✨ **Authentication System**
- User signup with email verification
- Flexible login (username or email)
- Password management and change functionality
- Secure session management

👤 **User Profile Management**
- User avatars with image upload
- Full name and email management
- Profile editing capabilities
- Password change option

📝 **Data Entry System**
- Create and manage entities (title + description)
- View entity history
- Delete entries
- User-specific data isolation

🎨 **Modern UI/UX**
- Dark modern theme
- Responsive design (mobile-friendly)
- Intuitive navigation with avatar dropdown
- Real-time form validation feedback

⚙️ **Django Admin**
- Full admin interface for user and entity management
- Advanced filtering and search capabilities
- Batch operations support

## Project Structure

```
projectfolder/
├── DataEntryProject/          # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── DataEntry/                 # Main application
│   ├── models.py             # Database models (UserProfile, Entity)
│   ├── views.py              # View functions
│   ├── forms.py              # Django forms
│   ├── admin.py              # Admin configuration
│   ├── signals.py            # Django signals
│   ├── urls.py               # App URL patterns
│   ├── apps.py               # App configuration
│   └── migrations/           # Database migrations
├── templates/                 # HTML templates
│   ├── base.html             # Base template with navigation
│   └── DataEntry/
│       ├── login.html        # Login page
│       ├── signup.html       # Registration page
│       ├── home.html         # Dashboard/Data entry
│       ├── profile.html      # User profile
│       ├── profile_edit.html # Profile editing
│       ├── change_password.html
│       ├── entity_detail.html
│       └── entity_confirm_delete.html
├── static/                    # Static files
│   └── css/
│       └── style.css         # Main stylesheet (dark theme)
├── media/                     # User uploads (avatars)
├── manage.py                  # Django management script
└── db.sqlite3                 # SQLite database
```

## Installation & Setup

### 1. **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)

### 2. **Install Dependencies**

```bash
pip install django pillow
```

**OR** if using a requirements file:

```bash
pip install -r requirements.txt
```

### 3. **Navigate to Project Directory**

```bash
cd ../projectfolder
```

### 4. **Run Migrations** (Already Done)

If you're setting up fresh:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. **Create Superuser (Admin Account)**

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username: `admin`
- Email: `admin@example.com`
- Password: `(enter a secure password)`

### 6. **Run Development Server**

```bash
python manage.py runserver
```

The server will start at: `http://localhost:8000/`

## Usage Guide

### **Accessing the Application**

1. **Landing/Login Page**: `http://localhost:8000/login/`
   - Login with username/email and password
   - Or click "Sign up here" to create a new account

2. **Home/Dashboard**: `http://localhost:8000/` (after login)
   - Add new data entries
   - View your entry history
   - Delete entries

3. **Profile Page**: Click avatar → "My Profile"
   - View your profile information
   - Click "Edit Profile" to modify details
   - Click "Change Password" to update password

4. **Logout**: Click avatar → "Logout"
   - Ends your session securely

### **Admin Panel**

1. Access: `http://localhost:8000/admin/`
2. Login with superuser credentials
3. Manage:
   - Users and their profiles
   - All data entries
   - User permissions

## Database Models

### **UserProfile**
- **user**: OneToOne relationship with Django's User model
- **full_name**: User's display name
- **avatar**: Profile image (optional)
- **created_at**: Account creation timestamp
- **updated_at**: Last profile update timestamp

### **Entity**
- **user**: Foreign key to User (data owner)
- **title**: Entry title (required)
- **description**: Entry content/details
- **created_at**: Entry creation time
- **updated_at**: Last modification time

## API Endpoints

| URL | Method | Purpose | Auth Required |
|-----|--------|---------|---|
| `/login/` | GET/POST | User login | No |
| `/signup/` | GET/POST | User registration | No |
| `/logout/` | GET | Logout | Yes |
| `/` | GET/POST | Dashboard/Data entry | Yes |
| `/profile/` | GET | View profile | Yes |
| `/profile/edit/` | GET/POST | Edit profile | Yes |
| `/profile/change-password/` | GET/POST | Change password | Yes |
| `/entity/<id>/` | GET | View entry details | Yes |
| `/entity/<id>/delete/` | GET/POST | Delete entry | Yes |
| `/admin/` | GET/POST | Admin panel | Admin only |

## Features Breakdown

### **Authentication Flow**
1. New user signs up with: full name, username, email, password, avatar (optional)
2. User profile is automatically created via Django signals
3. User logs in with username OR email + password
4. Session is established and stored in database
5. Logout terminates session and redirects to login

### **Data Entry Flow**
1. Authenticated user fills two fields: Title and Description
2. Click "Save Entry" button
3. Data is saved to database with user association
4. Entry appears in user's entry list
5. User can view or delete entries anytime

### **Profile Management**
1. Avatar dropdown in navigation bar
2. Click avatar to see dropdown menu
3. Two options:
   - "My Profile" → View/Edit profile
   - "Logout" → End session
4. Profile edit allows:
   - Change full name
   - Change email
   - Update avatar
5. Separate "Change Password" option

## Styling & Theme

The application uses a **dark modern theme** with:
- Dark navy background (#0f172a)
- Slate-colored cards (#1e293b)
- Indigo primary color (#6366f1)
- Smooth transitions and hover effects
- Responsive grid layouts
- Mobile-optimized design

### **Color Palette**
```css
Primary:     #6366f1
Danger:      #ef4444
Success:     #10b981
Dark BG:     #0f172a
Card BG:     #1e293b
Text:        #f1f5f9
Secondary:   #64748b
```

## Troubleshooting

### **Port Already in Use**
```bash
python manage.py runserver 8001
```

### **Database Errors**
```bash
python manage.py migrate --run-syncdb
```

### **Static Files Not Loading**
```bash
python manage.py collectstatic
```

### **Avatar Not Uploading**
- Ensure media folder exists: `..\media\`
- Check file permissions
- Verify DEBUG=True in settings.py

## Security Notes

⚠️ **Development Only**: The DEBUG setting is True. For production:

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'generate-new-secret-key'
```

## Next Steps / Future Enhancements

- [ ] Email verification on signup
- [ ] Password reset via email
- [ ] Two-factor authentication
- [ ] Data export features
- [ ] Search functionality for entries
- [ ] Entry categories/tags
- [ ] Sharing entries with other users
- [ ] API endpoints (DRF)
- [ ] WebSocket for real-time updates
- [ ] Dark/Light theme toggle

## Support

For issues or questions, refer to:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Forms Documentation](https://docs.djangoproject.com/en/5.2/topics/forms/)
- [Django Models Documentation](https://docs.djangoproject.com/en/5.2/topics/db/models/)

---

**Created with Django 5.2.13**
**Version 1.0.0**
