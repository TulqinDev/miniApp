from rest_framework.routers import DefaultRouter

from data.file.views import FileViewSet

router = DefaultRouter()
router.register(r"", FileViewSet)

urlpatterns = router.urls
