import unittest
from src.parking_lot_system.parking_lot import ParkingLot

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        pass

    def test_singleton_1(self):
        parking_lot_1 = ParkingLot(6)
        parking_lot_2 = ParkingLot(1)
        self.assertEqual(parking_lot_1, parking_lot_2)

    def tearDown(self):
        pass