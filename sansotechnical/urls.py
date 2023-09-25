from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from . import views
rout = DefaultRouter()
rout.register(r'customers', views.Customers, basename="GetAllCustomers")
rout.register(r'almasystemsmodels', views.AlmaSystemModels, basename='AlmaSystemModels')

urlpatterns = [
    path('', include(rout.urls), name='testview' )

]