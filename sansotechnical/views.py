from rest_framework import viewsets
from .models import  Customers, Alma_Systems_Models
from .serializers import Customers_Ser, Alma_Systems_Models_Ser

class Customers(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('internal_id')
    serializer_class = Customers_Ser

class AlmaSystemModels(viewsets.ModelViewSet):
    queryset = Alma_Systems_Models.objects.all().order_by('model_name')
    serializer_class = Alma_Systems_Models_Ser
    

