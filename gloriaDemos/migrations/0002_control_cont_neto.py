# Generated by Django 4.2.1 on 2023-06-05 17:28

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gloriaDemos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control_cont_neto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('turno', models.CharField(blank=True, max_length=50)),
                ('lote', models.CharField(blank=True, max_length=50)),
                ('linea_maq', models.CharField(blank=True, max_length=150)),
                ('tanque', models.CharField(blank=True, max_length=50)),
                ('tipo_leche', models.CharField(blank=True, max_length=50)),
                ('operador', models.IntegerField(choices=[])),
                ('supervisor', models.IntegerField(choices=[])),
                ('caracteristica', models.CharField(blank=True, max_length=200)),
                ('especificacion', models.CharField(blank=True, max_length=170)),
                ('carta', models.CharField(blank=True, max_length=50)),
                ('frec_muestreo', models.CharField(blank=True, max_length=150)),
                ('tam_muestra', models.CharField(blank=True, max_length=50)),
                ('observaciones', models.CharField(blank=True, max_length=300)),
                ('sub_grupo1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('sub_grupo2', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('sub_grupo3', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('sub_grupo4', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('sub_grupo5', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
        ),
    ]
