from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TaskViewSet, LabelViewSet, SlotViewSet, EmotionViewSet, TaskResultViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('labels', LabelViewSet)
router.register('slots', SlotViewSet)
router.register('emotions', EmotionViewSet)
router.register('task-results', TaskResultViewSet)

urlpatterns = [
    path('', include(router.urls))
]