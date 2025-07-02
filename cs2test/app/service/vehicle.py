from datetime import date
from cs2test.app.models import Vehicle
from cs2test.app.models.dto import vehicle

class Services:

    def build_vehicle(data: vehicle.VehicleDTO) -> Vehicle:
        return Vehicle(
            name=data.name,
            wheels=data.wheels,
            brand=data.brand,
            model=data.model,
            manufacture_date=data.manufacture_date,
            weight_kg=data.weight_kg,
            fuel=data.fuel,
            color=data.color,
            mileage=data.mileage,
            transmission=data.transmission,
            ipva=data.ipva,
            sunroof=data.sunroof or False,
            nitro=data.nitro or False,
        )

    def save_vehicle(data: vehicle.VehicleDTO) -> Vehicle:
        vehicle = Services.build_vehicle(data)
        vehicle.save()
        return vehicle
