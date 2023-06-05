# Generated by Django 4.2.1 on 2023-06-05 17:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gloriaDemos', '0002_control_cont_neto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control_cont_neto',
            name='operador',
            field=models.IntegerField(choices=[(1, 'admin')]),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='sub_grupo1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='sub_grupo2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='sub_grupo3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='sub_grupo4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='sub_grupo5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='control_cont_neto',
            name='supervisor',
            field=models.IntegerField(choices=[(1, 'admin')]),
        ),
    ]