from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from .models import Alma_Systems_Models, HP_Models, HP_Details, Alma_Systems, Customers
from .serializers import (
    Alma_Systems_Models_Ser, HP_Models_Ser, HP_Details_Ser, Alma_Systems_Ser, Customers_Ser
)

class AllModelsListSerializer(serializers.Serializer):
    # Define fields for your custom list serializer
    alma_systems_models = Alma_Systems_Models_Ser(many=True)
    hp_models = HP_Models_Ser(many=True)
    hp_details = HP_Details_Ser(many=True)
    alma_systems = Alma_Systems_Ser(many=True)
    customers = Customers_Ser(many=True)

class AllModelsViewSet(viewsets.ModelViewSet):
    queryset = None  # Set to None to avoid queryset errors
    serializer_class = AllModelsListSerializer  # Set a default serializer class

    def get_serializer_class(self):
        # Determine the serializer class based on the action
        if self.action == 'list':
            # Use a custom serializer for the list action
            return AllModelsListSerializer
        else:
            # For other actions (create, retrieve, update, delete), return None or your default serializer class
            return AllModelsListSerializer

    def list(self, request):
        # Implement the list operation to retrieve data from all models
        alma_systems_models = Alma_Systems_Models.objects.all()
        hp_models = HP_Models.objects.all()
        hp_details = HP_Details.objects.all()
        alma_systems = Alma_Systems.objects.all()
        customers = Customers.objects.all()

        # Serialize the data for each model
        alma_systems_models_data = Alma_Systems_Models_Ser(alma_systems_models, many=True).data
        hp_models_data = HP_Models_Ser(hp_models, many=True).data
        hp_details_data = HP_Details_Ser(hp_details, many=True).data
        alma_systems_data = Alma_Systems_Ser(alma_systems, many=True).data
        customers_data = Customers_Ser(customers, many=True).data

        # Combine the data into a single response
        response_data = {
            'alma_systems_models': alma_systems_models_data,
            'hp_models': hp_models_data,
            'hp_details': hp_details_data,
            'alma_systems': alma_systems_data,
            'customers': customers_data,
        }

        return Response(response_data)

class GetAllCustomers(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = Customers_Ser
    

