from Vehicles.car import Car


def create_vehicle(vehicle_type, brand, model, fuel_consumption,
                   plate_number, price_hour, price_day, price_week):
    if vehicle_type == 'car':
        return Car(brand, model, fuel_consumption, plate_number, price_hour, price_day, price_week)
    else:
        raise NotImplementedError('Vehicle type not supported.')
