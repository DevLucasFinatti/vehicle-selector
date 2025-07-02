from django.db import models
from .enums import WheelEnum, BrandEnum, ModelEnum, FuelEnum, TransmissionEnum, IpvaEnum

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    wheels = models.CharField(max_length=10, choices=WheelEnum.choices)
    brand = models.CharField(max_length=20, choices=BrandEnum.choices)
    model = models.CharField(max_length=20, choices=ModelEnum.choices)
    manufacture_date = models.DateField()
    weight_kg = models.FloatField()
    fuel = models.CharField(max_length=10, choices=FuelEnum.choices)
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=20, choices=TransmissionEnum.choices)
    ipva = models.CharField(max_length=10, choices=IpvaEnum.choices)
    sunroof = models.BooleanField(default=False)
    nitro = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.color})'
