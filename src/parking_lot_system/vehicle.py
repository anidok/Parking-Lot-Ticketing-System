from abc import ABC
from .constants import VehicleType, Color


class Vehicle(ABC):
    def __init__(self, registration_number: str, vehicle_type: VehicleType, color: Color, ticket=None):
        self.__registration_number = registration_number
        self.__type = vehicle_type
        self.__color = color
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket

    def get_color(self):
        return self.__color

    def get_registration_number(self):
        return self.__registration_number


class Car(Vehicle):
    def __init__(self, registration_number: str, color: str, ticket=None):
        super().__init__(registration_number, VehicleType.CAR, Color[color], ticket)
