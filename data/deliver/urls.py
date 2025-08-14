from rest_framework import routers

from data.deliver.views import DeliverViewSet

router = routers.DefaultRouter()

router.register(r"", DeliverViewSet)


urlpatterns = router.urls