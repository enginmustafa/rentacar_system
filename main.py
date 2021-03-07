import json
from datetime import datetime

from Client.client import Client
from Constants import enums
from RentSystem.rent_result import RentResult
from Vehicles import vehicles_util
from RentSystem.rent_system import RentSystem


# load cars from json to system
def load_cars(rent_system: RentSystem):
    vehicles = vehicles_util.load_vehicles_from_json()

    for vehicle in vehicles:
        rent_system.add_car(vehicle)


# Extract information from result of rent request
def print_rent_result(result: RentResult):
    if result.success:
        result_message = '[Rent successful] Sum to collect from client: ' + \
                         str(result.sum_with_applied_discount()) + '.'

        # Check if discount applied, convert discount for visual preferences
        # 0.7 = 30%, 0.9 = 10%
        if result.discount != 1:
            result_message = result_message + ' Applied discount: ' + \
                             str(float("{:.2f}".format((1 - result.discount) * 100))) + '%.'
    else:
        result_message = '[Rent not successful] ' + result.error_message

    print(result_message + '\n')


def main():
    # Generate dict of cars and export it to json for further usage
    # Run if not created json before
    # vehicles_util.generate_vehicles()

    rent_system = RentSystem()

    # load cars from json file to system
    load_cars(rent_system)

    # create clients which will rent cars
    ivan = Client('Ivan')
    alex = Client('Alex')

    # add clients to rent system
    rent_system.add_client(ivan)
    rent_system.add_client(alex)

    # show available cars on system
    for car in rent_system.available_cars():
        print(car.to_dict())

    # rent car with plate 0005 for ivan, from 2021/03/03 10:00 to 2021/03/05 10:00
    print_rent_result(
        rent_system.rent_car(ivan, ['0005'], enums.Units.DAY, datetime(2021, 3, 3, 10), 2))

    # try to rent car with plate 0005 for alex, from 2021/03/03 11:00 to 2021/03/05 11:00
    print_rent_result(
        rent_system.rent_car(alex, ['0005'], enums.Units.DAY, datetime(2021, 3, 3, 10), 2))

    # rent cars with specified plate numbers for ivan, from 2021/03/03 23:00 to 2021/03/04 02:00
    print_rent_result(
        rent_system.rent_car(ivan, ['0000', '0001', '0002', '0004'], enums.Units.HOUR, datetime(2021, 3, 3, 23), 3))

    # try rent cars with specified plate numbers for alex, from 2021/03/04 01:59 to 2021/03/11 01:59
    print_rent_result(
        rent_system.rent_car(ivan, ['0000', '0001', '0002', '0004'], enums.Units.WEEK, datetime(2021, 3, 4, 1, 59), 1))

    # rent cars with specified plate numbers for alex, from 2021/03/04 03:00 to 2021/03/11 03:00
    print_rent_result(
        rent_system.rent_car(ivan, ['0000', '0001', '0002', '0004'], enums.Units.WEEK, datetime(2021, 3, 4, 2, 1), 1))


if __name__ == '__main__':
    main()
