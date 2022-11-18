import unittest
from models import Station, Customer


class test_notify(unittest.TestCase):

    def test_notify(self):
        customer = Customer
        station = Station
        station.attach(self=station, customer=customer)
        station.notify(self=station, customer=customer)

        self.assertEqual(customer.satisfaction, True)
