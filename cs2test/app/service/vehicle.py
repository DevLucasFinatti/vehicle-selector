from datetime import date

from django.forms import model_to_dict
from cs2test.app.models import Vehicle
from cs2test.app.models.responses import Response as ApiResponse
from cs2test.app.service.vehicle import Services
from cs2test.app.models.dto.vehicle import VehicleDTO

import json

class Services:
    # def create_vehicles_test():
    #     with open('caminho/para/o/arquivo.json', 'r', encoding='utf-8') as f:
    #         data = json.load(f)
    #         print(data)


    def build_vehicle(data: VehicleDTO) -> Vehicle:
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

    def save_vehicle(data: VehicleDTO) -> Vehicle:
        vehicle = Services.build_vehicle(data)
        vehicle.save()
        return vehicle

    def create_vehicles(vehicleDtoList: list[VehicleDTO]):
        try:
            vehicles = []
            for vehicleDto in vehicleDtoList:
                vehicle = Services.save_vehicle(vehicleDto)
                vehicle_dict = model_to_dict(vehicle)
                vehicles.append(vehicle_dict)

            return ApiResponse.CreatedResponse(data=vehicles).to_drf_response()

        except KeyError as e:
            return ApiResponse.ErrorResponse(
                message={"error": f"Missing field: {str(e)}"},
                status_code=400
            ).to_drf_response()

        except ValueError as e:
            return ApiResponse.ErrorResponse(
                message={"error": f"Invalid value: {str(e)}"},
                status_code=400
            ).to_drf_response()

        except Exception as e:
            return ApiResponse.ErrorResponse(
                message={"error": str(e)},
                status_code=500
            ).to_drf_response()
