from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet, RoleViewSet, StatusViewSet, UserViewSet, TaskViewSet, LabelViewSet, SlotViewSet, EmotionViewSet, TaskResultViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('labels', LabelViewSet)
router.register('slots', SlotViewSet)
router.register('emotions', EmotionViewSet)
router.register('task-results', TaskResultViewSet)
router.register('statuses', StatusViewSet)
router.register('comments', CommentViewSet)
router.register('roles', RoleViewSet)


urlpatterns = [
    path('', include(router.urls))
]