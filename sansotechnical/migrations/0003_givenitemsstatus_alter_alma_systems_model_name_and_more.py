# Generated by Django 4.2.4 on 2023-09-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sansotechnical', '0002_alter_alma_systems_models_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GivenItemsStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statuses', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='alma_systems',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Alma_model_name', to='sansotechnical.alma_systems_models'),
        ),
        migrations.AlterField(
            model_name='hp_details',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HP_model_name', to='sansotechnical.hp_models'),
        ),
        migrations.CreateModel(
            name='CustomersHaveSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemGivenDate', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customers_Have', to='sansotechnical.customers')),
                ('systemGivenStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Given_Status', to='sansotechnical.givenitemsstatus')),
                ('systemItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='System_Items', to='sansotechnical.alma_systems')),
            ],
        ),
        migrations.CreateModel(
            name='customersHaveHP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hpGivenDate', models.DateField()),
                ('detachedDate', models.DateField(blank=True)),
                ('hp1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP1', to='sansotechnical.hp_details')),
                ('hp1GivenStatus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP1_Given_Status', to='sansotechnical.givenitemsstatus')),
                ('hp2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP2', to='sansotechnical.hp_details')),
                ('hp2GivenStatus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP2_Given_Status', to='sansotechnical.givenitemsstatus')),
                ('hp3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP3', to='sansotechnical.hp_details')),
                ('hp3GivenStatus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP3_Given_Status', to='sansotechnical.givenitemsstatus')),
                ('hp4', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP4', to='sansotechnical.hp_details')),
                ('hp4GivenStatus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP4_Given_Status', to='sansotechnical.givenitemsstatus')),
                ('hp5', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP5', to='sansotechnical.hp_details')),
                ('hp5GivenStatus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='HP5_Given_Status', to='sansotechnical.givenitemsstatus')),
            ],
        ),
    ]
