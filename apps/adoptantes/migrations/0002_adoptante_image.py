# Generated by Django 3.0.5 on 2020-06-17 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptante',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='adoptantes/images'),
        ),
    ]
