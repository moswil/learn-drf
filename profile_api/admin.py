"""Admin site for our user's profile."""
from django.contrib import admin

from profile_api.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Customized admin view of the UserProfile Model."""

    list_display = ('email', 'name',
                    'is_active', 'is_staff',)
