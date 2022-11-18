import unittest
from models import Customer


class test_update(unittest.TestCase):

    def test_update(self):
        customer = Customer
        customer.update(self=customer)

        self.assertEqual(customer.satisfaction, True)
