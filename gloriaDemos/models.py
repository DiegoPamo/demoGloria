from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#Operador, Supervisor y Administrador
class User(AbstractUser):
    is_operador = models.BooleanField(default= False)
    is_supervisor = models.BooleanField(default= False)
    is_administrador = models.BooleanField(default= False)
    picture = models.ImageField(default='/media/user.png',upload_to='media/')
