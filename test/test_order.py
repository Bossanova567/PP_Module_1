import unittest
import main
from models import Customer, Driver

class test_order(unittest.TestCase):

    async def test_order(self):
        customer: Customer ={ "customer": { "id": "ce5f6b5d-4e98-4fc0-90d7-163de769e06c", "name": "string",
                                            "point_A": "string", "point_B": "string", "load_weight": 110,
                                            "trailer_type": "string", "satisfaction": False}
        }
        driver: Driver = {"driver": { "id": "ce5f6b5d-4e98-4fc0-90d7-163de769e06c", "name": "string",
                                      "delivery_status": False}
                          }
        result = await main.order(customer, driver)

        self.assertEqual(result[0]['satisfaction'], True)

