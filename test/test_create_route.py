import unittest
import main
from models import Customer, Driver

class test_create_route(unittest.TestCase):

    async def test_create_route(self):

        result = await main.create_route("Lviv", "Berlin", {
  "point_A": "string",
  "point_B": "string",
  "distance": 0,
  "travel_time": 0
})

        self.assertAlmostEqual(result.distance, 929, 10)

