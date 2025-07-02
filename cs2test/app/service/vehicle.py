from datetime import date
from app.models import Vehicle
from app.models.dto import vehicle

class Services:

    def build_vehicle(data: vehicle.VehicleDTO) -> Vehicle:
        return Vehicle(
            name=data.get(data.name),
            wheels=data.get(data.wheels),
            brand=data.get(data.brand),
            model=data.get(data.model),
            manufacture_date=data.get(data.manufacture_date),
            weight_kg=data.get(data.weight_kg),
            fuel=data.get(data.fuel),
            color=data.get(data.color),
            mileage=data.get(data.mileage),
            transmission=data.get(data.transmission),
            ipva=data.get(data.ipva),
            sunroof=data.get("sunroof", False),
            nitro=data.get("nitro", False),
        )

    def save_vehicle(data: vehicle.VehicleDTO) -> Vehicle:
        vehicle = Services.build_vehicle(data)
        vehicle.save()
        return vehicle
