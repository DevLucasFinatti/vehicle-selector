from rest_framework.decorators import api_view
from rest_framework.request import Request

from cs2test.app.models.responses import Response as ApiResponse
from cs2test.app.service.vehicle import Services
from django.http import HttpResponse

from cs2test.app.models.dto.vehicle import VehicleDTO
from cs2test.app.models.enums import BrandEnum, FuelEnum, IpvaEnum, ModelEnum, TransmissionEnum, WheelEnum


@api_view(['POST'])
def create_vehicle(request: Request):
    try:
        body = request.data

        dto = VehicleDTO(
            name=body["name"],
            wheels=WheelEnum(body["wheels"]),
            brand=BrandEnum(body["brand"]),
            model=ModelEnum(body["model"]),
            manufacture_date=body["manufacture_date"],
            weight_kg=body["weight_kg"],
            fuel=FuelEnum(body["fuel"]),
            color=body["color"],
            mileage=body["mileage"],
            transmission=TransmissionEnum(body["transmission"]),
            ipva=IpvaEnum(body["ipva"]),
            sunroof=body.get("sunroof", False),
            nitro=body.get("nitro", False),
        )

        vehicle = Services.save_vehicle(dto)

        return ApiResponse.CreatedResponse(data=vehicle).to_drf_response()

    except KeyError as e:
        return ApiResponse.ErrorResponse(message={"error": f"Missing field: {str(e)}"}, status_code=400).to_drf_response()
    except ValueError as e:
        return ApiResponse.ErrorResponse(message={"error": f"Invalid value: {str(e)}"}, status_code=400).to_drf_response()
    except Exception as e:
        return ApiResponse.ErrorResponse(message={"error": str(e)}, status_code=500).to_drf_response()
