from django.urls import path
from . import views
from .views import UserRegistrationView, UserLoginView, UserDetailView, UserDeleteView, UserUpdateView

urlpatterns = [
    # User URLs
    path('users/register/', UserRegistrationView.as_view(), name='register'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # Project URLs
    path('projects/', views.ProjectListView.as_view(), name='list_projects'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:id>/', views.ProjectRetrieveView.as_view(), name='retrieve_project'),
    path('projects/<int:id>/update/', views.ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:id>/delete/', views.ProjectDeleteView.as_view(), name='delete_project'),

    # Task URLs
    path('projects/<int:project_id>/tasks/', views.TaskListView.as_view(), name='list_tasks'),
    path('projects/<int:project_id>/tasks/create/', views.TaskCreateView.as_view(), name='create_task'),
    path('tasks/<int:id>/', views.TaskRetrieveView.as_view(), name='retrieve_task'),
    path('tasks/<int:id>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks/<int:id>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),

    # Comment URLs
    path('tasks/<int:task_id>/comments/', views.CommentListView.as_view(), name='list_comments'),
    path('tasks/<int:task_id>/comments/create/', views.CommentCreateView.as_view(), name='create_comment'),
    path('comments/<int:id>/', views.CommentRetrieveView.as_view(), name='retrieve_comment'),
    path('comments/<int:id>/update/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('comments/<int:id>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
