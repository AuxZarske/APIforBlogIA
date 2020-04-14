from django.shortcuts import render

# Create your views here.


def numRol(rol):
    rol = str(rol)
    roles = ['anonymous', 'registered','registeredVIP', 'gestor', 'admin'] 
    try:
        num = roles.index(rol)
    except:
        num = -1

    return num