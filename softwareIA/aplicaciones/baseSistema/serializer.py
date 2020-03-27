from .models import TipoIA
from rest_framework import serializers


class TipoIASerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoIA
        fields = '__all__' 

    def validate_title(self,data):
        typesIA = list(TipoIA.objects.filter(title = data))
        if len(typesIA) != 0:
            raise serializers.validationError("Ese título ya esta registrado")
        else:
            return data
