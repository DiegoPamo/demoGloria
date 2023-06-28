# Generated by Django 4.2.1 on 2023-06-21 17:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gloriaDemos', '0004_control_cont_neto_hora_reg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='control_cont_neto',
            name='cilindro1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='control_cont_neto',
            name='cilindro2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='control_cont_neto',
            name='cilindro3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]
