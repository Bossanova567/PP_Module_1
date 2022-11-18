import unittest
from models import Station, Customer


class test_attach(unittest.TestCase):

    def test_attach(self):
        customer = Customer
        station = Station
        station.attach(self=station, customer=customer)


        self.assertNotEqual(station.customers, 0)
        self.assertNotEqual(station.customers.count(customer), 0)
