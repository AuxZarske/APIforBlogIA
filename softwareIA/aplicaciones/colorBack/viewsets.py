

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import RedColor, ColorInfo
from .serializer import RedColorSerializer, ColorSerializer
from .views import deleteRedIA

class RedColorViewSet(viewsets.ModelViewSet):
    queryset = RedColor.objects.filter(id = 0)
    serializer_class = RedColorSerializer 

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
    serializer_class = ColorSerializer 
    #queryset = ColorInfo.objects.all()
    def get_queryset(self):
        idRed = self.request.query_params.get('red', None)
        return ColorInfo.objects.filter(red = idRed)
    
        
    