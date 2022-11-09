from django.contrib import admin
from adpanel.models import UserProfile

# Register your models here.

@admin.register(UserProfile)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

