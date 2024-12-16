from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Project, Task, Comment, ProjectMember

# Get the custom User model
User = get_user_model()

# Register custom User model with a customized UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the User list
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Search by username, email, etc.
    ordering = ('id',)

    # Fields to display when viewing/editing a User
    fieldsets = (
        (None, {'fields': ('username', 'password')}), 
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to display when adding a new User
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )

# Register Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at', 'owner')

# Register Task model
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date')
    search_fields = ('title', 'assigned_to__username', 'project__name')
    list_filter = ('status', 'priority', 'project', 'assigned_to')

# Register Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'task', 'created_at')
    search_fields = ('content', 'user__username', 'task__title')
    list_filter = ('created_at', 'task')

# Register ProjectMember model
@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'role')
    search_fields = ('user__username', 'project__name')
    list_filter = ('role', 'project')
