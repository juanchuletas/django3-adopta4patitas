# Generated by Django 3.0.5 on 2020-06-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_mascota_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
