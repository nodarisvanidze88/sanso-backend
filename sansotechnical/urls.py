from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from . import views
rout = DefaultRouter()
rout.register(r'customers', views.Customer, basename="GetAllCustomers")
rout.register(r'almasystemsmodels', views.AlmaSystemModels, basename='AlmaSystemModels')
rout.register(r'hpmodels', views.HPModels, basename="hpmodels")
rout.register(r'almasystems', views.AlmaSystems, basename="almasystems")
rout.register(r'techpersons', views.TechnicalPerson, basename="techpersons")

urlpatterns = [
    path('', include(rout.urls), name='testview' )

]