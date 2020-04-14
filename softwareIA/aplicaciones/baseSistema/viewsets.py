from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.response import Response
from django.http import Http404
# from rest_framework.authentication import TokenAuthentication
from .models import TipoIA, User, AppDjango
from .serializer import TipoIASerializer, UserSerializer, AppDjangoSerializer

from .permission import IsAdminUser, IsLoggedInUserOrAdmin, IsAdminOrAnonymousUser, IsAnonymousUser, IsGestorUser, IsRegisteredUser, IsRegisteredVIPUser



class AppDjangoSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = AppDjango.objects.all()
    serializer_class = AppDjangoSerializer 

    def get_permissions(self): #tiene que ser el admin
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser|IsRegisteredUser|IsRegisteredVIPUser|IsGestorUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        try:         
            instance = self.get_object()
            # obtener nombre
            nameApp = instance.nombreApp
            print(nameApp)
            self.perform_destroy(instance)
            listArt = list(TipoIA.objects.filter(componentApp = nameApp))
            if len(listArt) != 0:
                for art in listArt:
                    try:
                        inst = TipoIA.objects.get(id = art.id)
                        inst.componentApp = ''
                        inst.save()
                    except:
                        pass
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

 
class TipoIAViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    # authentication_class = (TokenAuthentication,)
    queryset = TipoIA.objects.all()
    serializer_class = TipoIASerializer 

    def get_permissions(self):
        print('si aca')
        print(self.action)
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser|IsGestorUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser|IsRegisteredUser|IsRegisteredVIPUser|IsGestorUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminUser|IsRegisteredUser|IsRegisteredVIPUser|IsGestorUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser|IsGestorUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser|IsGestorUser]

        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all() #menos yo
    serializer_class = UserSerializer
    #authentication_classes = [TokenAuthentication] #cambiar al otro
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):        
        return User.objects.all().exclude(username = self.request.user) 

    def get_permissions(self): #tiene que ser el admin
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]