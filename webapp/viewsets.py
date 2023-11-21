from rest_framework import viewsets

from webapp.models import Sensor, Actuador, Lectura, Escritura, Cliente, ClienteSensor, ClienteActuador
from webapp.serializers import SensorSerializer, ActuadorSerializer, LecturaSerializer, EscrituraSerializer, \
    ClienteSerializer, ClienteSensorSerializer, ClienteActuadorSerializer


class SensorViewSet(viewsets.ModelViewSet):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class ActuadorViewSet(viewsets.ModelViewSet):
	queryset = Actuador.objects.all()
	serializer_class = ActuadorSerializer


class LecturaViewSet(viewsets.ModelViewSet):
	queryset = Lectura.objects.all()
	serializer_class = LecturaSerializer


class EscrituraViewSet(viewsets.ModelViewSet):
	queryset = Escritura.objects.all()
	serializer_class = EscrituraSerializer


class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer



class ClienteSensorViewSet(viewsets.ModelViewSet):
	queryset = ClienteSensor.objects.all()
	serializer_class = ClienteSensorSerializer



class ClienteActuadorViewSet(viewsets.ModelViewSet):
	queryset = ClienteActuador.objects.all()
	serializer_class = ClienteActuadorSerializer