from rest_framework.routers import DefaultRouter

from core.views import TodoViewSet


router = DefaultRouter()
router.register('todos', TodoViewSet)

urlpatterns = router.urls
