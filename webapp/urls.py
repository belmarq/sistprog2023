from django.urls import path
from rest_framework import routers

from webapp.viewsets import SensorViewSet, ActuadorViewSet, LecturaViewSet, EscrituraViewSet, ClienteViewSet, \
    ClienteSensorViewSet, ClienteActuadorViewSet

route = routers.SimpleRouter()

route.register('sensor', SensorViewSet)
route.register('actuador', ActuadorViewSet)
route.register('lectura', LecturaViewSet)
route.register('escritura', EscrituraViewSet)
route.register('cliente', ClienteViewSet)
route.register('cliente-sensor', ClienteSensorViewSet)
route.register('cliente-actuador', ClienteActuadorViewSet)

urlpatterns = route.urls

