from .models import RedColor, ColorInfo
from rest_framework import serializers
from .views import crearRed, entrenarRed



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorInfo
        fields = ['red','backgroundColor', 'textColor']
    
    def create(self, validate_data):
        instance = ColorInfo()
        instance.backgroundColor = validate_data.get('backgroundColor')
        instance.textColor = validate_data.get('textColor')
        instance.red = validate_data.get('red')
        idRed = instance.red.id
        color = instance.backgroundColor
        texto = instance.textColor
        resp = entrenarRed(idRed, color, texto)
        if resp == 0:
            #si ta bien guardar
            instance.save()
            return instance
        raise serializers.validationError("Error")




class RedColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedColor
        fields = '__all__' 
    
    def create(self, validate_data):
        instance = RedColor()
        instance.save() 
        num = instance.id
        resp = crearRed(num) 
        if resp != 0:
            instance.delete()

        return instance


