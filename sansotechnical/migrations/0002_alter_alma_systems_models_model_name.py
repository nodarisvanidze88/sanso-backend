# Generated by Django 4.2.5 on 2023-09-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sansotechnical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alma_systems_models',
            name='model_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
