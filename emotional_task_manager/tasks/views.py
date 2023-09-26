from rest_framework import viewsets
from .models import User, Task, Label, Slot, Emotion, TaskResult, Role
from .serializers import UserSerializer, TaskSerializer, LabelSerializer, SlotSerializer, EmotionSerializer, TaskResultSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer

class TaskResultViewSet(viewsets.ModelViewSet):
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer