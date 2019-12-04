from typing import Dict, Optional, List, Tuple
from .vehicle import Vehicle
from .parking_ticket import ParkingTicket
from .constants import Color
from .exception import ParkingFullException


class ParkingLot(object):   

    class __ParkingLot:
        def __init__(self, max_slot_count: int):
            self.max_slot_count = max_slot_count

            self.current_slot_count = 0
            self.active_tickets: Dict[str, ParkingTicket] = {}
            self.available_slots = [1 for i in range(max_slot_count)]

    instance = None

    def __new__(cls, max_slot_count: int): # __new__ always a classmethod
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__ParkingLot(max_slot_count)
        return ParkingLot.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def next_available_slot(self):
        if self.is_full():
            raise ParkingFullException('Sorry, parking lot is full.')

        try:
            # Get the index of first available slot
            available_slot_index = self.available_slots.index(1)
            available_slot_number = available_slot_index + 1
            return available_slot_number
        except ValueError:
            raise ParkingFullException('Sorry, parking lot is full.')

    def issue_parking_ticket(self, vehicle: Vehicle) -> ParkingTicket:
        available_slot_number = self.next_available_slot()

        # Generate a new ticket
        ticket = ParkingTicket(available_slot_number, vehicle)
        vehicle.assign_ticket(ticket)

        self.available_slots[available_slot_number - 1] = 0
        self.increment_slot_count()
        self.active_tickets[ticket.get_ticket_number()] = ticket

        return ticket

    def is_full(self):
        return self.current_slot_count >= self.max_slot_count

    def increment_slot_count(self):
        self.current_slot_count = self.current_slot_count + 1

    def free_slot(self, slot_number: int):
        if not self.is_slot_valid(slot_number):
            raise Exception("Sorry, The provided slot doesn't exist")

        if self.is_slot_free(slot_number):
            raise Exception('The provided slot is already free')

        ticket = self.get_ticket_for_slot_number(slot_number)

        if ticket is None:
            raise Exception('Ticket not issued for current slot')

        self.active_tickets.pop(ticket.get_ticket_number())
        self.decrement_slot_count()
        # Mark the current slot as empty
        self.available_slots[slot_number - 1] = 1

    def is_slot_valid(self, slot_number: int):
        return slot_number <= self.max_slot_count

    def is_slot_free(self, slot_number: int):
        return self.available_slots[slot_number - 1] == 1

    def get_ticket_for_slot_number(self, slot_number: int) -> Optional[ParkingTicket]:
        for _, ticket in self.active_tickets.items():
            if isinstance(ticket, ParkingTicket):
                if ticket.get_slot_number() == slot_number:
                    return ticket

        return None

    def decrement_slot_count(self):
        self.current_slot_count = self.current_slot_count - 1

    def status(self) -> List[Tuple]:
        output: List[Tuple] = []

        for _, ticket in self.active_tickets.items():
            if isinstance(ticket, ParkingTicket):
                slot_number = ticket.get_slot_number()
                registration_number = ticket.get_vehicle().get_registration_number()
                color = ticket.get_vehicle().get_color()
                color_str = color.value

                # create a tuple
                record = (slot_number, registration_number, color_str)
                output.append(record)

        return output

    def get_registration_numbers_for_cars_with_colour(self, color: str) -> List[str]:
        registration_numbers: List[str] = []

        tickets = self.get_tickets_for_cars_with_colour(color)
        for ticket in tickets:
            registration_numbers.append(ticket.get_vehicle().get_registration_number())

        return registration_numbers

    def get_slot_numbers_for_cars_with_colour(self, color: str) -> List[int]:
        slot_numbers: List[int] = []

        tickets = self.get_tickets_for_cars_with_colour(color)
        for ticket in tickets:
            slot_numbers.append(ticket.get_slot_number())

        return slot_numbers

    def get_tickets_for_cars_with_colour(self, color: str) -> List[ParkingTicket]:
        tickets: List[ParkingTicket] = []

        for _, ticket in self.active_tickets.items():
            if isinstance(ticket, ParkingTicket):
                current_color = ticket.get_vehicle().get_color()

                if current_color == Color[color.upper()]:
                    tickets.append(ticket)

        return tickets

    def get_slot_number_for_registration_number(self, registration_number: str) -> Optional[int]:
        ticket = self.get_ticket_for_car_with_registration_number(registration_number)

        return None if ticket is None else ticket.get_slot_number()

    def get_ticket_for_car_with_registration_number(self, registration_number: str) -> Optional[ParkingTicket]:
        for _, ticket in self.active_tickets.items():
            if isinstance(ticket, ParkingTicket):
                current_registration_number = ticket.get_vehicle().get_registration_number()

                if current_registration_number == registration_number:
                    return ticket

        return None