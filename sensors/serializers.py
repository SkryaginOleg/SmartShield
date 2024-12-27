from rest_framework import serializers
from .models import Sensor, SensorLog

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'type', 'location', 'status']

class SensorLogSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SensorLog
        fields = ['id', 'sensor', 'value', 'timestamp', 'exceeded_threshold']

class CreateSensorLogSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField(help_text="ID сенсора")
    value = serializers.FloatField(help_text="Значення для нового логу")