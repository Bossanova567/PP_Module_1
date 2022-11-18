import unittest
from models import Customer, Driver


class test_deliver(unittest.TestCase):

    def test_deliver(self):
        driver = Driver
        driver.deliver(self=driver)

        self.assertEqual(driver.delivery_status, True)
