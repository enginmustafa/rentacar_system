from datetime import datetime
from Vehicles.car import Car


class RentCard:

    def __init__(self, car: Car, rent_from: datetime, rent_to: datetime):
        self._car = car
        self._rent_from = rent_from
        self._rent_to = rent_to

    def _same_car(self, plate_number) -> bool:
        return self._car.plate_number == plate_number

    # Check if a period(date A to date B) intersects with period of RentCard for specific car by plate number
    def car_in_use(self, plate_number, date_from: datetime, date_to: datetime) -> bool:
        result = False

        if self._same_car(plate_number):
            result = (self._rent_from <= date_from <= self._rent_to or self._rent_from <= date_to <= self._rent_to)

        return result
