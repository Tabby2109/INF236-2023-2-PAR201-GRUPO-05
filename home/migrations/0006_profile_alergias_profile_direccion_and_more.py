# Generated by Django 5.0.4 on 2024-05-06 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rayos_x_tipo_de_examen_alter_rayos_x_fecha_reserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='alergias',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rut',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='tramo_fonasa',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='ecografias',
            name='fecha_reserva',
            field=models.DateField(default=datetime.datetime(2024, 5, 6, 21, 34, 13, 562386, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='rayos_x',
            name='fecha_reserva',
            field=models.DateField(default=datetime.datetime(2024, 5, 6, 21, 34, 13, 560170, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='resonancias',
            name='fecha_reserva',
            field=models.DateField(default=datetime.datetime(2024, 5, 6, 21, 34, 13, 563416, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tomografias',
            name='fecha_reserva',
            field=models.DateField(default=datetime.datetime(2024, 5, 6, 21, 34, 13, 562386, tzinfo=datetime.timezone.utc)),
        ),
    ]