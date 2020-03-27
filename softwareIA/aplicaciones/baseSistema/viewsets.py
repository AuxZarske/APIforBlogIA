from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # <-- Here
# from rest_framework.authentication import TokenAuthentication
from .models import TipoIA
from .serializer import TipoIASerializer

class TipoIAViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    # authentication_class = (TokenAuthentication,)
    queryset = TipoIA.objects.all()
    serializer_class = TipoIASerializer 