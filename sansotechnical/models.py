from tkinter import CASCADE
from typing import Any
from django.db import models


class Alma_Systems_Models(models.Model):
    model_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.model_name

class HP_Models(models.Model):
    model_name = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name
    
class HP_Details(models.Model):
    model_name = models.ForeignKey(HP_Models, on_delete=models.CASCADE, blank=False, related_name="HP_model_name")
    hp_serial_number = models.CharField(max_length=20)
    hp_manufacturing_date = models.DateField()
    size = models.FloatField()

    def __str__(self):
        return f'{self.model_name} - {self.hp_serial_number}'


class Alma_Systems(models.Model):
    model_name = models.ForeignKey(Alma_Systems_Models, on_delete=models.CASCADE, blank=False, related_name="Alma_model_name")
    system_serial_number = models.CharField(max_length=20)
    manufacturing_date = models.DateField()

    def __str__(self):
        return f'{self.model_name} - {self.system_serial_number}'

class GivenItemsStatus(models.Model):
    statuses = models.CharField(max_length=50)

    def __str__(self):
        return self.statuses


class Customers(models.Model):
    internal_id = models.CharField(max_length=10) # This number is of internal our company registry number
    name = models.CharField(max_length=100)
    indetification_code = models.CharField(max_length=11)
    address = models.CharField(max_length=200, blank=True)
    contact_person = models.CharField(max_length=200, blank=True)
    contact_person_mobile = models.CharField(max_length=20, blank=True)
    clinic_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.internal_id} - {self.name}'

class CustomersHaveSystem(models.Model):
    systemGivenDate = models.DateField(blank=False)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=False, related_name="Customers_Have")
    systemItem = models.ForeignKey(Alma_Systems, on_delete=models.CASCADE, blank=False, related_name="System_Items")
    systemGivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, blank=False, related_name="Given_Status")

    def __str__(self):
        return f"{self.customer} - {self.systemItem}"

class customersHaveHP(models.Model):
    hpGivenDate = models.DateField(blank=False)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=False, null=True, related_name="HP_Customer")
    hp1 = models.ForeignKey(HP_Details, on_delete=models.CASCADE, blank=True, null=True, related_name="HP1")
    hp1GivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="HP1_Given_Status")
    hp2 = models.ForeignKey(HP_Details, on_delete=models.CASCADE, blank=True, null=True, related_name="HP2")
    hp2GivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="HP2_Given_Status")
    hp3 = models.ForeignKey(HP_Details, on_delete=models.CASCADE, blank=True, null=True, related_name="HP3")
    hp3GivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="HP3_Given_Status")
    hp4 = models.ForeignKey(HP_Details, on_delete=models.CASCADE, blank=True, null=True, related_name="HP4")
    hp4GivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="HP4_Given_Status")
    hp5 = models.ForeignKey(HP_Details, on_delete=models.CASCADE, blank=True, null=True, related_name="HP5")
    hp5GivenStatus = models.ForeignKey(GivenItemsStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="HP5_Given_Status")
    detachedDate = models.DateField(blank=True, null=True)

    def __str__(self):
        self.returnedValue = []
        self.currentValues = f"{self.hp1} {self.hp2} {self.hp3} {self.hp4} {self.hp5}".split()

        for self.i in self.currentValues:
            print(self.i)
            if self.i is not None:
                self.returnedValue.append(self.i)
                
        

        return " ".join(self.returnedValue)





