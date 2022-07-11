import re

from rest_framework import serializers

from backend.models import Equipment, EquipmentType


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        if not re.match(r'^[a-zA-Z0-9-_@]*$', data['serial']):
            raise serializers.ValidationError('Invalid serial number')
        return data

    class Meta:
        model = Equipment
        fields = ['name', 'manufacturer',
                  'equipment_type', 'description', 'serial']


class EquipmentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ['name', 'description']
