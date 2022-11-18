import unittest
from models import Station, Customer


class test_detach(unittest.TestCase):

    def test_detach(self):
        customer = Customer
        station = Station
        station.attach(self=station, customer=customer)
        station.detach(self=station, customer=customer)


        self.assertEqual(station.customers, 0)
        self.assertEqual(station.customers.count(customer), 0)
