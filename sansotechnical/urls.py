from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from . import views
rout = DefaultRouter()
rout.register(r'allinfo', views.AllModelsViewSet, basename="testview")
rout.register(r'customers', views.GetAllCustomers, basename="GetAllCustomers")

urlpatterns = [
    path('', include(rout.urls), name='testview' )

]