from django.db import models
from datetime import datetime, date, time, timedelta

# Create your models here.

class RedColor(models.Model):
    id = models.AutoField(primary_key = True)
    #path = models.FileField(upload_to='Archivos/Grupo/7777') 
    

class ColorInfo(models.Model):
    id = models.AutoField(primary_key = True)
    backgroundColor = models.CharField('identificador color de fondo', max_length = 50, null = False, blank = False)
    textColor = models.CharField('identificador color de texto', max_length = 50, null = False, blank = False)
    red = models.ForeignKey(RedColor, on_delete = models.CASCADE,  null = True, blank = True)