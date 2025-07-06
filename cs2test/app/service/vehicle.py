from datetime import date, datetime
import unicodedata
import os

from django.forms import model_to_dict
from cs2test.app.models import Vehicle
from cs2test.app.models.responses import Response as ApiResponse
from cs2test.app.models.dto.vehicle import VehicleDTO

import json

from cs2test.app.service.pages import Page

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

    def standarization(texto: str) -> str:
        texto = texto.lower().replace(" ", "")
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
        return texto
    
    def search_vehicle_by_brand_name(input: str):
        try:
            search = Services.standarization(input)
            results = []

            for vehicle in Vehicle.objects.all():
                brand = vehicle.brand or ""
                name = vehicle.name or ""

                key1 = Services.standarization(brand + name)
                key2 = Services.standarization(name + brand)

                if search in key1 or search in key2:
                    results.append(model_to_dict(vehicle))

            return results

        except Exception as e:
            return ApiResponse.ErrorResponse(
                message={"error": str(e)},
                status_code=500
            ).to_drf_response()
            
            
    def search_vehicle(input: str):
        try:
            search = Services.standarization(input)
            results = []

            for vehicle in Vehicle.objects.all():
                vehicle_dict = model_to_dict(vehicle)

                combined_fields = ""
                for value in vehicle_dict.values():
                    if value is not None:
                        combined_fields += str(value)

                standardized_combined = Services.standarization(combined_fields)

                if search in standardized_combined:
                    results.append(vehicle_dict)

            return results

        except Exception as e:
            return ApiResponse.ErrorResponse(
                message={"error": str(e)},
                status_code=500
            ).to_drf_response()
            
    def search_vehicle_by_profile(perfil):
        try:
            perfil = Services.standarization(perfil)

            perfil_model_map = {
                "conan": ["PICKUP", "OFFROAD"],
                "paidefamilia": ["SUV", "MINIVAN", "SEDAN"],
                "garotao": ["HATCH", "SPORT", "COMPACT"],
                "fino": ["LUXURY", "ELECTRIC", "SEDAN"]
            }

            if perfil not in perfil_model_map:
                return ApiResponse.ErrorResponse(
                    message={"error": f"Perfil '{perfil}' não encontrado"},
                    status_code=404
                ).to_drf_response()

            modelos = perfil_model_map[perfil]

            vehicles = Vehicle.objects.filter(model__in=modelos)
            results = [model_to_dict(vehicle) for vehicle in vehicles]

            return results

        except Exception as e:
            return ApiResponse.ErrorResponse(
                message={"error": str(e)},
                status_code=500
            ).to_drf_response()

    def format_vehicle_list(vehicles: list[dict]) -> list[dict]:
        result = []
        for v in vehicles:
            result.append({
                "nome": v["name"],
                "marca": v["brand"],
                "ano": v["manufacture_date"].year,
                "nitro": v["nitro"],
                "teto_solar": v["sunroof"],
                "tipo_combustivel": v["fuel"]
            })
        return result
    
    def form_response(src_result):
        for result in src_result:
            print("════════════════════════════════════")
            print(f"Nome: {result['name']}")
            print(f"Marca: {result['brand']}")
            print(f"Modelo: {result['model']}")
            print(f"Ano: {result['manufacture_date'].year}")
            print(f"Cor: {result['color']}")
            print(f"Combustível: {result['fuel']}")
            print(f"Teto Solar: {'Sim' if result['sunroof'] else 'Não'}")
            print(f"Nitro: {'Sim' if result['nitro'] else 'Não'}")

        print("═════════════════════════════════════")
        print('Estes são os resultados da busca')
        print('Para prosseguir, digite qualquer coisa')
        input(": ")

    def load_and_create_vehicles_from_json(filepath):
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Arquivo {filepath} não encontrado")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                vehicles_data = json.load(f)
            
            created_vehicles = []
            for data in vehicles_data:
                try:
                    # Debug: Mostra os dados que estão sendo processados
                    print(f"Processando veículo: {data.get('name', 'sem nome')}")
                    
                    # Conversão da data
                    if isinstance(data['manufacture_date'], str):
                        manufacture_date = datetime.fromisoformat(data['manufacture_date']).date()
                    else:
                        manufacture_date = data['manufacture_date']
                    
                    # Criação do DTO com tratamento de valores nulos
                    dto = VehicleDTO(
                        name=data['name'],
                        wheels=data['wheels'],
                        brand=data['brand'],
                        model=data['model'],
                        manufacture_date=manufacture_date,
                        weight_kg=float(data['weight_kg']),
                        fuel=data['fuel'],
                        color=data['color'],
                        mileage=int(data['mileage']),
                        transmission=data['transmission'],
                        ipva=data['ipva'],
                        sunroof=bool(data.get('sunroof', False)),
                        nitro=bool(data.get('nitro', False)),
                    )
                    
                    # Debug: Mostra o DTO criado
                    print(f"DTO criado: {dto.__dict__}")
                    Page.wait(5)
                    
                    # Salva o veículo
                    vehicle = Services.save_vehicle(dto)
                    created_vehicles.append(vehicle)
                    
                    # Debug: Confirmação de salvamento
                    print(f"Veículo salvo com ID: {vehicle.id}")
                    
                except Exception as e:
                    print(f"Erro ao processar veículo {data.get('name', 'desconhecido')}")
                    print(f"Detalhes do erro: {str(e)}")
                    print(f"Dados problemáticos: {data}")
                    continue
            
            return created_vehicles
        
        except Exception as e:
            print(f"Erro ao carregar arquivo JSON: {str(e)}")
            raise 
