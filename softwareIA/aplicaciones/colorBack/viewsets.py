

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # <-- Here

from .models import RedColor, ColorInfo
from .serializer import RedColorSerializer, ColorSerializer
from .views import deleteRedIA
from softwareIA.aplicaciones.baseSistema.permission import IsAdminUser, NoHaveCompPerm
from softwareIA.aplicaciones.baseSistema.models import AppDjango
from softwareIA.aplicaciones.baseSistema.views import numRol

class RedColorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = RedColor.objects.filter(id = 0)
    serializer_class = RedColorSerializer 

    def get_permissions(self): 
        permission_classes = []
        rolUser = self.request.user.groups
        nameApp = self.__module__.split('.')
        nameApp = str(nameApp[2])
        rolApp = list(AppDjango.objects.filter(nombreApp = nameApp))
        if len(rolApp) != 0: 
            numRolApp = numRol(rolApp[0].rol)
            numRolUser = numRol(rolUser) 
            if numRolApp <= numRolUser:
                pass # no se imponen restricciones de uso, permiso aceptado
            else:
                permission_classes = [NoHaveCompPerm]
        else:
            permission_classes = [NoHaveCompPerm]

        return [permission() for permission in permission_classes]



    def destroy(self, request, *args, **kwargs):
        try:
        
            instance = RedColor.objects.filter(id = self.kwargs['pk'])
            cant = len(list(instance))
            print(instance)
            if cant != 0:

                res = deleteRedIA(self.kwargs['pk'])  #captar error, sino elimina, no borrar base datos
                if res == 0:
                    self.perform_destroy(instance)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        except:
            
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)

class ColorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    serializer_class = ColorSerializer 
    #queryset = ColorInfo.objects.all()
    def get_queryset(self):
        idRed = self.request.query_params.get('red', None)
        return ColorInfo.objects.filter(red = idRed)
    
    
    def get_permissions(self): 
        permission_classes = []
        rolUser = self.request.user.groups
        nameApp = self.__module__.split('.')
        nameApp = str(nameApp[2])
        rolApp = list(AppDjango.objects.filter(nombreApp = nameApp))
        if len(rolApp) != 0: 
            numRolApp = numRol(rolApp[0].rol)
            numRolUser = numRol(rolUser) 
            if numRolApp <= numRolUser:
                pass # no se imponen restricciones de uso, permiso aceptado
            else:
                permission_classes = [NoHaveCompPerm]
        else:
            permission_classes = [NoHaveCompPerm]

        return [permission() for permission in permission_classes]
    