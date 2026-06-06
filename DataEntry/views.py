from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import UserProfile, Entity
from .forms import SignUpForm, LoginForm, EntityForm, UserProfileForm, AvatarForm, PasswordChangeForm


def signup_view(request):
    """Handle user signup"""
    if request.user.is_authenticated:
        return redirect('DataEntry:home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('DataEntry:home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    
    return render(request, 'DataEntry/signup.html', {'form': form})


def login_view(request):
    """Handle user login with username or email"""
    if request.user.is_authenticated:
        return redirect('DataEntry:home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            
            # Try to find user by username first, then by email
            user = None
            try:
                # Try username
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                # Try email
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    messages.error(request, 'Invalid username/email or password.')
                    return render(request, 'DataEntry/login.html', {'form': form})
            
            # Authenticate the user
            if user and user.check_password(password):
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('DataEntry:home')
            else:
                messages.error(request, 'Invalid username/email or password.')
    else:
        form = LoginForm()
    
    return render(request, 'DataEntry/login.html', {'form': form})


def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('DataEntry:login')


@login_required(login_url='DataEntry:login')
def home_view(request):
    """Main page with data entry form"""
    if request.method == 'POST':
        form = EntityForm(request.POST)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.user = request.user
            entity.save()
            messages.success(request, 'Data saved successfully!')
            return redirect('DataEntry:home')
    else:
        form = EntityForm()
    
    # Get user's entities
    entities = Entity.objects.filter(user=request.user)
    user_profile = request.user.profile if hasattr(request.user, 'profile') else None
    
    context = {
        'form': form,
        'entities': entities,
        'user_profile': user_profile,
    }
    return render(request, 'DataEntry/home.html', context)


@login_required(login_url='DataEntry:login')
def profile_view(request):
    """Display user profile and update avatar"""
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    avatar_form = AvatarForm(request.POST or None, request.FILES or None, instance=user_profile)
    if request.method == 'POST':
        if avatar_form.is_valid():
            avatar_form.save()
            messages.success(request, 'Avatar updated successfully!')
            return redirect('DataEntry:profile')
        else:
            for field, errors in avatar_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    context = {
        'user_profile': user_profile,
        'user': request.user,
        'avatar_form': avatar_form,
    }
    return render(request, 'DataEntry/profile.html', context)


@login_required(login_url='DataEntry:login')
def profile_edit_view(request):
    """Edit user profile"""
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save()
            # Update email if provided
            if request.POST.get('email'):
                request.user.email = request.POST.get('email')
                request.user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('DataEntry:profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserProfileForm(instance=user_profile)
        form.fields['email'].initial = request.user.email
    
    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'DataEntry/profile_edit.html', context)


@login_required(login_url='DataEntry:login')
def change_password_view(request):
    """Change user password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            if not user.check_password(form.cleaned_data['old_password']):
                messages.error(request, 'Current password is incorrect.')
            else:
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('DataEntry:profile')
    else:
        form = PasswordChangeForm()
    
    context = {'form': form}
    return render(request, 'DataEntry/change_password.html', context)


@login_required(login_url='DataEntry:login')
def entity_detail_view(request, pk):
    """View entity details"""
    entity = get_object_or_404(Entity, pk=pk, user=request.user)
    context = {'entity': entity}
    return render(request, 'DataEntry/entity_detail.html', context)


@login_required(login_url='DataEntry:login')
def entity_delete_view(request, pk):
    """Delete an entity"""
    entity = get_object_or_404(Entity, pk=pk, user=request.user)
    if request.method == 'POST':
        entity.delete()
        messages.success(request, 'Entity deleted successfully!')
        return redirect('DataEntry:home')
    return render(request, 'DataEntry/entity_confirm_delete.html', {'entity': entity})
