from django.contrib import admin
from . import models
# Register your models here.
admin.site.register({
    models.Alma_Systems, 
    models.Alma_Systems_Models, 
    models.Customers, 
    models.HP_Details, 
    models.HP_Models,
    models.GivenItemsStatus,
    models.CustomersHaveSystem,
    models.customersHaveHP,
    models.TechnicalPersons,
    })