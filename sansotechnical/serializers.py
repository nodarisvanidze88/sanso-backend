from rest_framework import serializers
from . import models

class Alma_Systems_Models_Ser(serializers.ModelSerializer):
    class Meta:
        model = models.Alma_Systems_Models
        fields = '__all__'
        

class HP_Models_Ser(serializers.ModelSerializer):
    class Meta:
        model = models.HP_Models
        fields = '__all__'
    
class HP_Details_Ser(serializers.ModelSerializer):
    class Meta:
        model = models.HP_Details
        fields = '__all__'

class Alma_Systems_Ser(serializers.ModelSerializer):
    model_name = Alma_Systems_Models_Ser()
    class Meta:
        model = models.Alma_Systems
        fields = ['id', 'system_serial_number', 'manufacturing_date', 'model_name']


class Customers_Ser(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'

class TechnicalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TechnicalPersons
        fields = ['id','person_name']
