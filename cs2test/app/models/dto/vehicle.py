from dataclasses import dataclass
from datetime import date
from typing import Optional
from ..enums import WheelEnum, BrandEnum, ModelEnum, FuelEnum, TransmissionEnum, IpvaEnum

@dataclass
class VehicleDTO:
    name: str
    wheels: WheelEnum
    brand: BrandEnum
    model: ModelEnum
    manufacture_date: date
    weight_kg: float
    fuel: FuelEnum
    color: str
    mileage: int
    transmission: TransmissionEnum
    ipva: IpvaEnum
    sunroof: Optional[bool] = False
    nitro: Optional[bool] = False
