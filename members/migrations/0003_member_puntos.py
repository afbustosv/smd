# Generated by Django 4.1.3 on 2022-12-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]