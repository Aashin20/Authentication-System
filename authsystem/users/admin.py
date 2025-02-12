from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class UsersAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active', 'created_at')
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, UsersAdmin)