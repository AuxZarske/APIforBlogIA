from django.db import models
from datetime import datetime, date, time, timedelta

# Create your models here.

class TipoIA(models.Model):
    
    title = models.CharField(max_length = 50)
    src = models.URLField(max_length=300, default = "https://source.unsplash.com/UUjxTEET0c0/1200x560")
    description = models.TextField()
    componentApp = models.CharField(max_length = 70, null = True, blank = True)
    #creationDate =  models.DateField('creation date', auto_now=False,auto_now_add=True)
    #tags, 
    # secciones(image or text or video)

