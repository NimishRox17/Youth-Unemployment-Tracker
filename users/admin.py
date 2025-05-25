from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # Renamed to avoid conflict
from .models import User, Survey # Ensure this is Survey

@admin.register(User)
class UserAdmin(BaseUserAdmin): # Changed from CustomUserAdmin to UserAdmin for consistency
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2', 'first_name', 'last_name'), # Ensure password fields match AbstractUser
        }),
    )

@admin.register(Survey) # Ensure this is Survey
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'state', 'education', 'employment_status', 'created_at') # Changed status to employment_status
    list_filter = ('state', 'education', 'employment_status') # Changed status to employment_status
    search_fields = ('name', 'state')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age', 'gender')
        }),
        ('Location', {
            'fields': ('state',)
        }),
        ('Education & Employment', {
            'fields': ('education', 'employment_status', 'monthly_income', 'job_search_duration') # Changed status, jobtype
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ('created_at',)
        return ()