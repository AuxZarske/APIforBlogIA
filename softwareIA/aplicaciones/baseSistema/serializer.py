from .models import TipoIA, User, AppDjango
from rest_framework import serializers


class AppDjangoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppDjango
        fields = ('id', 'nombreApp', 'rol')
        extra_kwargs = {'id': {'read_only': True}}

    def validate_nombreApp(self,data):
        typesIA = list(AppDjango.objects.filter(nombreApp = data))
        typeMethod = str(self.context['request'].method)
        if len(typesIA) != 0 and typeMethod == 'POST':
            raise serializers.validationError("Ese nombre ya esta registrado")
        else:
            return data

    def validate_rol(self,data):
        permiso = 1
        if data == 'admin' or data == 'gestor' or data == 'registered' or data == 'anonymous' or data == 'registeredVIP':
            permiso = 0
        if permiso != 0:
            raise serializers.validationError("Rol inexistente")
        else:
            return data

    def update(self, instance, validated_data):
        instance.rol = validated_data.get('rol', instance.rol) 
        instance.save()
        return instance

    

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

    def create(self, validated_data):
        art = TipoIA.objects.create(**validated_data)
        nameApp = str(validated_data['componentApp'])

        if nameApp == '':
            art.save()
        else:
            listaAppEqual = list(AppDjango.objects.filter(nombreApp = nameApp))
            if len(listaAppEqual) != 0:
                art.save()
            else:
                art.delete()
                raise serializers.validationError("Ese componente ya no existe")
        return art

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'groups', 'email')
        model = User
        extra_kwargs = {'password': {'write_only': True}, 'username': {'read_only': True}, 'id': {'read_only': True}, 'email': {'read_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user
    