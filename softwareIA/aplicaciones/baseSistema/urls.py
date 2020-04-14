from rest_framework import routers

from .viewsets import TipoIAViewSet, UserViewSet, AppDjangoSet

router = routers.SimpleRouter()

router.register('tipoIAs', TipoIAViewSet)
router.register('AppsDj', AppDjangoSet)

router.register(r'manageUsers', UserViewSet, basename='userDataSist')

urlpatterns = router.urls