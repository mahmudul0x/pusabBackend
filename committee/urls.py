from rest_framework.routers import DefaultRouter

from .views import EcMemberViewSet

router = DefaultRouter()
router.register("committee", EcMemberViewSet, basename="committee")

urlpatterns = router.urls
