# Generated by Django 4.2.4 on 2023-09-12 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sansotechnical', '0004_alter_customershavehp_detacheddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customershavehp',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP_Customer', to='sansotechnical.customers'),
        ),
    ]
