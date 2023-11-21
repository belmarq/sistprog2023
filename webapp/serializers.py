from rest_framework import serializers

from webapp.models import Sensor, Actuador, Lectura, Escritura, Cliente, ClienteSensor, ClienteActuador


class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = '__all__'


class ActuadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actuador
		fields = '__all__'


class LecturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lectura
		fields = '__all__'


class EscrituraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Escritura
		fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = '__all__'


class ClienteSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClienteSensor
		fields = '__all__'

class ClienteActuadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClienteActuador
		fields = '__all__'
