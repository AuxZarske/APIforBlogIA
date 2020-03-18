from rest_framework import routers

from .viewsets import TipoIAViewSet

router = routers.SimpleRouter()
router.register('tipoIAs', TipoIAViewSet)

urlpatterns = router.urls