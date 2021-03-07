import string

from Constants import enums


class Car:

    def __init__(self, brand, model, fuel_consumption, plate_number, price_hour, price_day, price_week):
        self.brand = brand
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.plate_number = plate_number
        self.price_hour = price_hour
        self.price_day = price_day
        self.price_week = price_week

    def __get_unit_price(self, unit: string):
        return {
            enums.Units.HOUR: self.price_hour,
            enums.Units.DAY: self.price_day,
            enums.Units.WEEK: self.price_week
        }[unit]

    def calculate_price(self, unit: string, units: int):
        return self.__get_unit_price(unit) * units

    def to_dict(self):
        return {"brand": self.brand,
                "model": self.model,
                "fuel_consumption": self.fuel_consumption,
                "plate_number": self.plate_number,
                "price_hour": self.price_hour,
                "price_day": self.price_day,
                "price_week": self.price_week}
