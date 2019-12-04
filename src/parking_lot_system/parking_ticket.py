import uuid
from .vehicle import Vehicle


class ParkingTicket:
    def __init__(self, slot_number: int, vehicle: Vehicle):
        # ticket number could have been taken as an incremented integer value but here I have gone with uuid
        self.__ticket_number = uuid.uuid1()
        self.__vehicle = vehicle
        self.__slot_number = slot_number

    def get_ticket_number(self):
        return self.__ticket_number

    def get_vehicle(self):
        return self.__vehicle

    def get_slot_number(self):
        return self.__slot_number
