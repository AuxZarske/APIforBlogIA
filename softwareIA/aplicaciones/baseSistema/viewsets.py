from rest_framework import viewsets

from .models import TipoIA
from .serializer import TipoIASerializer

class TipoIAViewSet(viewsets.ModelViewSet):
    queryset = TipoIA.objects.all()
    serializer_class = TipoIASerializer 