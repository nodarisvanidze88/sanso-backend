from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from . import views
rout = DefaultRouter()
rout.register(r'', views.AllModelsViewSet, basename="testview")
rout.register(r'c', views.GetAllCustomers, basename="GetAllCustomers")

urlpatterns = [
    path('', include(rout.urls), name='testview' )

]