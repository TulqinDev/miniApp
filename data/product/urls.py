from rest_framework.routers import DefaultRouter

from data.product.views import ProductViewSet

router = DefaultRouter()
router.register(r"", ProductViewSet)

urlpatterns = router.urls
