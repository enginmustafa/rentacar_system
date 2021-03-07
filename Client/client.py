from RentSystem.rent_card import RentCard
from datetime import datetime


class Client:

    def __init__(self, name):
        self._name = name
        self._rent_cards = []

    # Add rented car to collection
    def add_rent_card(self, rent_card: RentCard):
        self._rent_cards.append(rent_card)

    def is_currently_using_car(self, plate_number, date_from: datetime, date_to: datetime):
        result = False

        for card in self._rent_cards:
            if card.car_in_use(plate_number, date_from, date_to):
                result = True

        return result
