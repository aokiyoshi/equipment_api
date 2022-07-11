from django.db import models


class EquipmentType(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=144)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Equipment(models.Model):
    name = models.CharField(max_length=16)
    manufacturer = models.CharField(max_length=16)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    description = models.CharField(max_length=144)
    serial = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
