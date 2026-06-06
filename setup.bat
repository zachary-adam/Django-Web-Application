@echo off
REM Quick Setup Script for DataEntry Application (Windows)

echo ================================
echo DataEntry Application - Quick Setup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.8+
    exit /b 1
)

echo [OK] Python found

REM Install dependencies
echo.
echo [*] Installing dependencies...
python -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo X Failed to install dependencies
    exit /b 1
)

echo [OK] Dependencies installed

REM Run migrations
echo.
echo [*] Running database migrations...
python manage.py migrate --noinput

if errorlevel 1 (
    echo X Failed to run migrations
    exit /b 1
)

echo [OK] Database migrations complete

REM Create superuser
echo.
echo [*] Creating admin account...
echo.
echo Please enter admin account details:
python manage.py createsuperuser

if errorlevel 1 (
    echo X Failed to create superuser
    exit /b 1
)

REM Run development server
echo.
echo ================================
echo [OK] Setup Complete!
echo ================================
echo.
echo Starting development server...
echo.
echo Access the application at:
echo   Frontend: http://localhost:8000/login/
echo   Admin:    http://localhost:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
