import unittest
from src.parking_lot_system.parking_lot import ParkingLot
from src.parking_lot_system.vehicle import Car
from src.parking_lot_system.exception import ParkingFullException


class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot: ParkingLot = ParkingLot(6)

    def test_parking_lot_end_to_end(self):
        # issue some tickets successfully
        self.issue_ticket('KA-01-HH-1234', 'White')
        self.issue_ticket('KA-01-HH-9999', 'White')
        self.issue_ticket('KA-01-BB-0001', 'Black')

        # check if next available slot is 4th after allocating first 3 slots
        expected = 4
        actual = self.parking_lot.next_available_slot()
        self.assertEqual(expected, actual)

        # issue some more tickets and fill up to max size
        self.issue_ticket('KA-01-HH-7777', 'Red')
        self.issue_ticket('KA-01-HH-2701', 'Blue')
        self.issue_ticket('KA-01-HH-3141', 'Black')

        # Till here no slot should be avalable
        expected = None
        actual = self.parking_lot.next_available_slot()
        self.assertEqual(expected, actual)

        # free 4th slot and check if it's available
        self.parking_lot.free_slot(4)
        expected = 4
        actual = self.parking_lot.next_available_slot()
        self.assertEqual(expected, actual)


        tickets = self.parking_lot.status()
        ticket = tickets[0]
        self.assertEqual(1, ticket[0])
        self.assertEqual('KA-01-HH-1234', ticket[1])
        self.assertEqual('White', ticket[2])

        # assert for current status
        ticket = tickets[1]
        self.assertEqual(2, ticket[0])
        self.assertEqual('KA-01-HH-9999', ticket[1])
        self.assertEqual('White', ticket[2])

        ticket = tickets[2]
        self.assertEqual(3, ticket[0])
        self.assertEqual('KA-01-BB-0001', ticket[1])
        self.assertEqual('Black', ticket[2])

        ticket = tickets[3]
        self.assertEqual(5, ticket[0])
        self.assertEqual('KA-01-HH-2701', ticket[1])
        self.assertEqual('Blue', ticket[2])

        ticket = tickets[4]
        self.assertEqual(6, ticket[0])
        self.assertEqual('KA-01-HH-3141', ticket[1])
        self.assertEqual('Black', ticket[2])

        # issue next ticket so that parking lot is now full
        self.issue_ticket('KA-01-P-333', 'White')

        # Exception should be raised when attempted to issue next ticket as parking lot is full
        with self.assertRaises(ParkingFullException):
            self.issue_ticket('DL-12-AA-9999', 'White')

        # assert for registration numbers against color of the cars
        registration_numbers = self.parking_lot.get_registration_numbers_for_cars_with_colour('White')
        self.assertEqual('KA-01-HH-1234', registration_numbers[0])
        self.assertEqual('KA-01-HH-9999', registration_numbers[1])
        self.assertEqual('KA-01-P-333', registration_numbers[2])

        # assert for slot numbers against color of the cars
        slot_numbers = self.parking_lot.get_slot_numbers_for_cars_with_colour('White')
        self.assertEqual(1, slot_numbers[0])
        self.assertEqual(2, slot_numbers[1])
        self.assertEqual(4, slot_numbers[2])

        # assert for slot number assigned to a car for a particular registration number
        expected = 6
        actual = self.parking_lot.get_slot_number_for_registration_number('KA-01-HH-3141')
        self.assertEqual(expected, actual)

        actual = self.parking_lot.get_slot_number_for_registration_number('MH-04-AY-1111')
        self.assertIsNone(actual)

    def tearDown(self):
        pass

    def issue_ticket(self, reg_no: str, color: str) -> Car:
        car = Car(reg_no, color)
        self.parking_lot.issue_parking_ticket(car)
