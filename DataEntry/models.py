from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

# Create your models here.

class UserProfile(models.Model):
    """Extended user profile with avatar and additional info"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/', 
        default='avatars/default-avatar.png',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Profile"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class Entity(models.Model):
    """Data entry model for storing user-submitted data"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entities')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    class Meta:
        verbose_name = "Entity"
        verbose_name_plural = "Entities"
        ordering = ['-created_at']
