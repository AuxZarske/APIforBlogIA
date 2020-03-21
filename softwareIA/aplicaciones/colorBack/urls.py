from django.urls import path

from rest_framework import routers
from .viewsets import RedColorViewSet, ColorViewSet
router = routers.SimpleRouter()
 
router.register(r'redColors', RedColorViewSet, basename='color')
router.register(r'train', ColorViewSet, basename='red')


from .views import consultRedIA, deleteRedIA
urlpatterns = [
    path('consult/<int:id>/<str:color>', consultRedIA, name='consult'),
    path('delete/<int:id>', deleteRedIA, name='deleteIA'),
]

urlpatterns += router.urls



