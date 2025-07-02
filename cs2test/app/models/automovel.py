from django.db import models
from .enums import WheelEnum, BrandEnum, ModelEnum, FuelEnum, TransmissionEnum, IpvaEnum

class Automovel(models.Model):
    automovel_id = models.AutoField(primary_key=True)
    rodas = models.CharField(max_length=10, choices=WheelEnum.choices)
    marca = models.CharField(max_length=20, choices=BrandEnum.choices)
    modelo = models.CharField(max_length=20, choices=ModelEnum.choices)
    data_fabricacao = models.DateField()
    peso_kg = models.FloatField()
    combustivel = models.CharField(max_length=10, choices=FuelEnum.choices)
    cor = models.CharField(max_length=50)
    quilometragem = models.PositiveIntegerField()
    transmissao = models.CharField(max_length=20, choices=TransmissionEnum.choices)
    ipva = models.CharField(max_length=10, choices=IpvaEnum.choices)
    teto_solar = models.BooleanField(default=False)
    nitro = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.cor})'
