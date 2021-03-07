import decimal
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta

from Client.client import Client
from RentSystem.rent_card import RentCard
from RentSystem.rent_result import RentResult
from Vehicles.car import Car
from RentSystem import rent_util
from Constants import enums


class RentSystem:

    def __init__(self):
        self._available_cars = []
        self._clients = []

        # Useful while checking if car is available on system, without further iterating
        self._plate_numbers = []

    # Add rentable car to system
    def add_car(self, car: Car):
        if not rent_util.is_value_in_list(self._available_cars, car):
            self._available_cars.append(car)
            self._plate_numbers.append(car.plate_number)

    # Remove car from system, no longer rentable
    def remove_car(self, car: Car):
        if rent_util.is_value_in_list(self._available_cars, car):
            self._available_cars.remove(car)

    def add_client(self, client: Client):
        if not rent_util.is_value_in_list(self._clients, client):
            self._clients.append(client)

    def remove_client(self, client: Client):
        if rent_util.is_value_in_list(self._clients, client):
            self._clients.remove(client)

    def available_cars(self):
        return self._available_cars

    # Check if given plate numbers match with plate numbers of vehicles on system
    def __are_plate_numbers_valid(self, plate_numbers: [string]):
        return rent_util.are_values_in_list(self._plate_numbers, plate_numbers)

    def __is_unit_valid(self, unit: string) -> bool:
        units = set(item.value for item in enums.Units)

        return unit.value in units

    def __get_car(self, plate_number):
        for car in self._available_cars:
            if car.plate_number == plate_number:
                return car

    # Calculate end date of rent, from date + rent_for * rent_unit
    def __calculate_end_period(self, rent_unit, rent_from, rent_for) -> datetime:
        return {
            enums.Units.HOUR: rent_from + relativedelta(hours=rent_for),
            enums.Units.DAY: rent_from + relativedelta(days=rent_for),
            enums.Units.WEEK: rent_from + relativedelta(months=rent_for)
        }[rent_unit]

    def __are_vehicles_available_for_rent(self, vehicle_plate_numbers, rent_from, rent_to) -> bool:
        for plate_number in vehicle_plate_numbers:
            for client in self._clients:
                if client.is_currently_using_car(plate_number, rent_from, rent_to):
                    return False

        return True

    def __finalize_rent(self, client: Client, plate_numbers: [], rent_from, rent_to, rent_unit, rent_units) -> decimal:
        sum_to_collect = 0

        for plate_number in plate_numbers:
            car = self.__get_car(plate_number)
            rent_card = RentCard(car, rent_from, rent_to)

            sum_to_collect += car.calculate_price(rent_unit, rent_units)
            client.add_rent_card(rent_card)

        return sum_to_collect

    def rent_car(self,
                 client: Client,
                 # plate number/s of vehicle/s that client wants to order, can order multiple at once
                 vehicle_plate_numbers: [],
                 # hour/day/week
                 rent_unit: string,
                 # exact time from which client wants to rent vehicles/s
                 rent_from: datetime,
                 # how many units client wants to rent the car for,
                 # example: rent_from = 13:00, unit: hours, rent_for=3, rent car from 13:00 to 16:00(13+3)
                 rent_for: int) -> RentResult:

        rent_to = datetime(1, 1, 1)
        sum_to_collect = 0

        # discount if 3 or more vehicles at once
        sum_discount = 0.7 if len(vehicle_plate_numbers) > 3 else 1

        rent_result = RentResult(False, 0, sum_discount, None)

        if not rent_util.is_value_in_list(self._clients, client):
            rent_result.error_message = "Client not registered to system."
            return rent_result

        if not self.__are_plate_numbers_valid(vehicle_plate_numbers):
            rent_result.error_message = "Vehicle plate number/s does not match to of our vehicles."
            return rent_result

        if not self.__is_unit_valid(rent_unit):
            rent_result.error_message = "Rent unit is not supported."
            return rent_result

        rent_to = self.__calculate_end_period(rent_unit, rent_from, rent_for)

        if not self.__are_vehicles_available_for_rent(vehicle_plate_numbers, rent_from, rent_to):
            rent_result.error_message = "Vehicle/one of the vehicles is already rented for given date."
            return rent_result

        sum_to_collect = self.__finalize_rent(client, vehicle_plate_numbers, rent_from, rent_to, rent_unit, rent_for)

        rent_result.success = True
        rent_result.sum_to_collect = sum_to_collect

        return rent_result

