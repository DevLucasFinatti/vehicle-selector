from django.db import models
from django.utils.translation import gettext_lazy as _

class WheelEnum(models.TextChoices):
    TWO = 'TWO', _('two')
    FOUR = 'FOUR', _('four')
    SIX = 'SIX', _('six')
    OTHER = 'OTHER', _('other')

class BrandEnum(models.TextChoices):
    FORD = 'FORD', _('ford')
    CHEVROLET = 'CHEVROLET', _('chevrolet')
    FIAT = 'FIAT', _('fiat')
    TOYOTA = 'TOYOTA', _('toyota')
    HONDA = 'HONDA', _('honda')
    OTHER = 'OTHER', _('other')

class ModelEnum(models.TextChoices):
    SEDAN = 'SEDAN', _('sedan')
    HATCH = 'HATCH', _('hatchback')
    SUV = 'SUV', _('suv')
    PICKUP = 'PICKUP', _('pickup')
    OTHER = 'OTHER', _('other')

class FuelEnum(models.TextChoices):
    GASOLINE = 'GASOLINE', _('gasoline')
    DIESEL = 'DIESEL', _('diesel')
    ELECTRIC = 'ELECTRIC', _('electric')
    HYBRID = 'HYBRID', _('hybrid')
    ETHANOL = 'ETHANOL', _('ethanol')

class TransmissionEnum(models.TextChoices):
    MANUAL = 'MANUAL', _('manual')
    AUTOMATIC = 'AUTOMATIC', _('automatic')
    CVT = 'CVT', _('cvt')
    SEMI_AUTOMATIC = 'SEMI_AUTOMATIC', _('semi')

class IpvaEnum(models.TextChoices):
    PAID = 'PAID', _('paid')
    LATE = 'LATE', _('late')
    EXEMPT = 'EXEMPT', _('exempt')
