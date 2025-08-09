from rest_framework.routers import DefaultRouter

from data.category.views import CategoryViewSet

router = DefaultRouter()
router.register(r"", CategoryViewSet)

urlpatterns = router.urls
