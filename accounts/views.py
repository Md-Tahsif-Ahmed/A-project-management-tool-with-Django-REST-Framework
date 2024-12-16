from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from django.contrib.auth import get_user_model
from .models import Project, Task, Comment
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ProjectSerializer, TaskSerializer, CommentSerializer


User = get_user_model()

# Register User
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# Login User
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = serializer.validated_data['token']
            return Response({
                "message": "Login successful",
                "token": str(token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



# Retrieve User Details
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

# Update User Details
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

# Delete User
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]  # Only admin users can delete accounts


# List Projects (GET /api/projects/)
class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the current user as the project owner
        serializer.save(owner=self.request.user)


# Create Project (POST /api/projects/)
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the current user as the project owner
        serializer.save(owner=self.request.user)


# Retrieve Project (GET /api/projects/{id}/)
class ProjectRetrieveView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# Update Project (PUT/PATCH /api/projects/{id}/)
class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        project = self.get_object()
        # Ensure that the current user is either the project owner or an admin
        if project.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to edit this project.")
        serializer.save()


# Delete Project (DELETE /api/projects/{id}/)
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to delete this project.")
        instance.delete()


# List Tasks (GET /api/projects/{project_id}/tasks/)
class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        serializer.save(project_id=project_id)


# Create Task (POST /api/projects/{project_id}/tasks/)
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        serializer.save(project_id=project_id)


# Retrieve Task (GET /api/tasks/{id}/)
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


# Update Task (PUT/PATCH /api/tasks/{id}/)
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        task = self.get_object()
        # Ensure that the current user has permission to update the task
        if task.assigned_to != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to edit this task.")
        serializer.save()


# Delete Task (DELETE /api/tasks/{id}/)
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.assigned_to != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to delete this task.")
        instance.delete()


# List Comments (GET /api/tasks/{task_id}/comments/)
class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        serializer.save(task_id=task_id, user=self.request.user)


# Create Comment (POST /api/tasks/{task_id}/comments/)
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        serializer.save(task_id=task_id, user=self.request.user)


# Retrieve Comment (GET /api/comments/{id}/)
class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


# Update Comment (PUT/PATCH /api/comments/{id}/)
class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        comment = self.get_object()
        # Ensure that the current user has permission to update the comment
        if comment.user != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to edit this comment.")
        serializer.save()


# Delete Comment (DELETE /api/comments/{id}/)
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to delete this comment.")
        instance.delete()
