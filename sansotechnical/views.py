from rest_framework import viewsets
from .models import  Customers, Alma_Systems_Models, HP_Models, Alma_Systems, TechnicalPersons
from .serializers import Customers_Ser, Alma_Systems_Models_Ser, HP_Models_Ser, Alma_Systems_Ser, TechnicalPersonSerializer

class Customer(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('internal_id')
    serializer_class = Customers_Ser

class AlmaSystemModels(viewsets.ModelViewSet):
    queryset = Alma_Systems_Models.objects.all().order_by('model_name')
    serializer_class = Alma_Systems_Models_Ser

class HPModels(viewsets.ModelViewSet):
    queryset = HP_Models.objects.all().order_by('model_name_HP')
    serializer_class = HP_Models_Ser

class AlmaSystems(viewsets.ModelViewSet):
    queryset = Alma_Systems.objects.all()
    serializer_class= Alma_Systems_Ser

class TechnicalPerson(viewsets.ModelViewSet):
    queryset = TechnicalPersons.objects.all()
    serializer_class= TechnicalPersonSerializer
    

