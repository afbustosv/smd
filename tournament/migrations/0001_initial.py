# Generated by Django 4.1.3 on 2022-12-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentCup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('premio', models.CharField(max_length=20)),
                ('couta', models.IntegerField()),
                ('numero', models.SmallIntegerField()),
            ],
        ),
    ]