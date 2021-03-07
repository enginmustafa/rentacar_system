import json
from Vehicles import vehicle_factory
from Vehicles.car import Car


def write_to_file(file_content, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(file_content, f, ensure_ascii=False, indent=4)


def read_from_file(file_path):
    text = open(file_path, "r").read()

    return text


# Helper method to generate car objects to write to json for further usage
def generate_vehicles():
    cars = []
    factory = vehicle_factory

    cars.append(factory.create_vehicle('car', 'Audi', 'A3', 6, '0000', 6, 50, 280))
    cars.append(factory.create_vehicle('car', 'Audi', 'A4', 6.5, '0001', 6.5, 53, 291))
    cars.append(factory.create_vehicle('car', 'Audi', 'A6', 8, '0002', 8, 56, 305))
    cars.append(factory.create_vehicle('car', 'Audi', 'A8', 9, '0003', 9, 56, 300))
    cars.append(factory.create_vehicle('car', 'Audi', 'Q7', 9.5, '0004', 10, 49, 286))
    cars.append(factory.create_vehicle('car', 'Mercedes', 'A180', 5.9, '0005', 5, 35, 190))
    cars.append(factory.create_vehicle('car', 'Mercedes', 'B220', 6.3, '0006', 6, 39, 200))
    cars.append(factory.create_vehicle('car', 'Mercedes', 'C280', 8, '0007', 12, 66, 335))
    cars.append(factory.create_vehicle('car', 'Mercedes', 'Ml320', 12.6, '0008', 16, 90, 450))
    cars.append(factory.create_vehicle('car', 'Mercedes', 'G450', 14, '0009', 19, 140, 800))
    cars.append(factory.create_vehicle('car', 'BMW', '320', 6.3, '0010', 6.5, 53, 291))
    cars.append(factory.create_vehicle('car', 'BMW', '530', 7.9, '0011', 8.1, 52, 286))
    cars.append(factory.create_vehicle('car', 'BMW', '740', 8.9, '0012', 8.9, 55, 296))

    cars_dict = [c.to_dict() for c in cars]
    write_to_file(cars_dict, 'cars_data.json')


# Load and return dict of cars
def load_vehicles_from_json():
    file_content = read_from_file('cars_data.json')
    vehicles = json.loads(file_content)

    result = []

    for vehicle in vehicles:
        car_vehicle = Car(**vehicle)
        result.append(car_vehicle)

    return result

