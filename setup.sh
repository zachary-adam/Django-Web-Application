#!/bin/bash
# Quick Setup Script for DataEntry Application

echo "================================"
echo "DataEntry Application - Quick Setup"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8+"
    exit 1
fi

echo "✓ Python found"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"

# Run migrations
echo ""
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

if [ $? -ne 0 ]; then
    echo "❌ Failed to run migrations"
    exit 1
fi

echo "✓ Database migrations complete"

# Create superuser
echo ""
echo "👤 Creating admin account..."
echo ""
echo "Please enter admin account details:"
python manage.py createsuperuser

if [ $? -ne 0 ]; then
    echo "❌ Failed to create superuser"
    exit 1
fi

echo ""
echo "✓ Admin account created"

# Run development server
echo ""
echo "================================"
echo "✨ Setup Complete!"
echo "================================"
echo ""
echo "Starting development server..."
echo ""
echo "🌐 Access the application at:"
echo "   Frontend: http://localhost:8000/login/"
echo "   Admin:    http://localhost:8000/admin/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
