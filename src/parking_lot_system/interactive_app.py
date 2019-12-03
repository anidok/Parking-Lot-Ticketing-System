# pylint: disable=broad-except
import traceback
from parking_lot_system.parking_lot import ParkingLot
from parking_lot_system.vehicle import Car
from parking_lot_system.exception import ParkingFullException


class InteractiveApp:
    def create_parking_lot(self, input_command: str):
        try:
            max_slot_count = int(input_command.split(' ')[1])
            self.parking_lot: ParkingLot = ParkingLot(max_slot_count)
            print('Created a parking lot with {} slots.'.format(str(max_slot_count)))
        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    def park(self, input_command: str):
        try:
            input_command_splitted = input_command.split(' ')
            registration_number = input_command_splitted[1]
            color = input_command_splitted[2]
            color = color.upper()

            vehicle = Car(registration_number, color)
            assigned_ticket = self.parking_lot.issue_parking_ticket(vehicle)

            assigned_slot_number = assigned_ticket.get_slot_number()

            print('Allocated slot number: {}'.format(str(assigned_slot_number)))

        except ParkingFullException as exception:
            print(exception)

        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    def leave(self, input_command: str):
        try:
            input_command_splitted = input_command.split(' ')
            slot_number = int(input_command_splitted[1])
            self.parking_lot.free_slot(slot_number)
            print('Slot number {} is free'.format(str(slot_number)))
        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    def status(self):
        print('Slot No\t Registration No\t Color')
        records = self.parking_lot.status()

        for record in records:
            print(record)

    def registration_numbers_for_cars_with_colour(self, input_command: str):
        try:
            input_command_splitted = input_command.split(' ')
            color = input_command_splitted[1]

            registration_numbers = self.parking_lot.get_registration_numbers_for_cars_with_colour(color)
            if self.is_empty(registration_numbers):
                print('Not Found')
            else:
                print(registration_numbers)

        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    def slot_numbers_for_cars_with_colour(self, input_command: str):
        try:
            input_command_splitted = input_command.split(' ')
            color = input_command_splitted[1]

            slot_numbers = self.parking_lot.get_slot_numbers_for_cars_with_colour(color)

            if self.is_empty(slot_numbers):
                print('Not Found')
            else:
                print(slot_numbers)

        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    def slot_number_for_registration_number(self, input_command: str):
        try:
            input_command_splitted = input_command.split(' ')
            registration_number = input_command_splitted[1]

            slot_number = self.parking_lot.get_slot_number_for_registration_number(registration_number)

            if slot_number is None:
                print('Not Found')
            else:
                print(slot_number)

        except Exception as exception:
            print('Some Error Occured: {}'.format(str(exception)))
            traceback.print_exc()

    @staticmethod
    def is_empty(input_list):
        return len(input_list) == 0
