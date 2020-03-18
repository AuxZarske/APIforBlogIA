from django.urls import path
from .views import activarEntrenamiento, consultIA

urlpatterns = [
    path('start/', activarEntrenamiento, name='start'),
    path('consult/<int:id>/<str:color>', consultIA, name='consult'),
]