from django.contrib import admin
from .models import UserProfile, Entity

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'created_at')
    search_fields = ('user__username', 'full_name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Info', {'fields': ('user', 'full_name')}),
        ('Avatar', {'fields': ('avatar',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username', 'description')
    list_filter = ('created_at', 'user')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Entry Info', {'fields': ('user', 'title', 'description')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
