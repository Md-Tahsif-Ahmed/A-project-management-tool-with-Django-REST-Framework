from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Project, Task, Comment, ProjectMember

User = get_user_model()

# User Serializer for listing and displaying user details
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')

# User Registration Serializer for creating a new user
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# User Login Serializer for authenticating a user and returning a JWT token
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return {
            'user': UserSerializer(user).data,  # Returning serialized user data
            'token': str(RefreshToken.for_user(user).access_token)  # Ensure token is returned as a string
        }

# Project Serializer for listing, creating, and updating projects
class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)  # Display owner user details

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner', 'created_at')

# Task Serializer for tasks related to a project
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)  # Display assigned user details
    project = ProjectSerializer(read_only=True)  # Display project details

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date')

# Comment Serializer for comments on tasks
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Display comment user details
    task = TaskSerializer(read_only=True)  # Display task details

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'task', 'created_at')

# Project Member Serializer to manage project memberships
class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Display user details
    project = ProjectSerializer(read_only=True)  # Display project details

    class Meta:
        model = ProjectMember
        fields = ('id', 'project', 'user', 'role')
