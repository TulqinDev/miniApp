from rest_framework import routers

from data.location.views import LocationViewSet

router = routers.DefaultRouter()
router.register(r"", LocationViewSet)

urlpatterns = router.urls
