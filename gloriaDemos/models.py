from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.contrib.postgres.fields import ArrayField

# Operador, Supervisor y Administrador


class User(AbstractUser):
    is_operador = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)
    picture = models.ImageField(default='/user.png', upload_to='media/')


class Control_cont_neto(models.Model):
    USUARIO_CHOICES = [(usuario.id, usuario.username)
                       for usuario in User.objects.all()]

    fecha = models.DateField(default=date.today, blank=True, null=True)
    turno = models.CharField(max_length=50, blank=True)
    lote = models.CharField(max_length=50, blank=True)
    linea_maq = models.CharField(max_length=150, blank=True)
    tanque = models.CharField(max_length=50, blank=True)
    tipo_leche = models.CharField(max_length=50, blank=True)
    operador = models.IntegerField(choices=USUARIO_CHOICES)
    supervisor = models.IntegerField(choices=USUARIO_CHOICES)
    caracteristica = models.CharField(max_length=200, blank=True)
    especificacion = models.CharField(max_length=170, blank=True)
    carta = models.CharField(max_length=50, blank=True)
    frec_muestreo = models.CharField(max_length=150, blank=True)
    tam_muestra = models.CharField(max_length=50, blank=True)
    observaciones = models.CharField(max_length=300, blank=True)
    sub_grupo1 = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
    sub_grupo2 = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
    sub_grupo3 = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
    sub_grupo4 = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
    sub_grupo5 = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
