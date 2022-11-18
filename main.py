from uuid import uuid4
import openrouteservice
import requests
from pprint import pprint
import transport

from fastapi import FastAPI

import models

app = FastAPI()

client = openrouteservice.Client(key='5b3ce3597851110001cf624886ee32ca91bf4ade867401c4b2f1957e')

BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'




@app.post("/route/{origin}/{destination}")
async def create_route(origin: str, destination: str, route: models.Route = None):
    origin_response = requests.get(f"{BASE_URL}&city={origin}")
    origin_data = origin_response.json()
    origin_latitude = origin_data[0].get('lat')
    origin_longitude = origin_data[0].get('lon')

    destination_response = requests.get(f"{BASE_URL}&city={destination}")
    destination_data = destination_response.json()
    destination_latitude = destination_data[0].get('lat')
    destination_longitude = destination_data[0].get('lon')

    coordinates = [[float(origin_longitude), float(origin_latitude)],
                   [float(destination_longitude), float(destination_latitude)]]

    direction = client.directions(coordinates=coordinates, profile='driving-car', format='geojson')

    route.point_A = origin
    route.point_B = destination
    route.distance = direction['features'][0]['properties']['segments'][0]['distance'] * 0.001  # meters to kilometers
    route.travel_time = direction['features'][0]['properties']['segments'][0][
                            'duration'] * 0.000277778  # seconds to hours
    return route


@app.post("/order")
async def order(customer: models.Customer, driver: models.Driver):
    station = models.Station
    # create customer: name, A, B, weight, trailer_type (optional)
    station.customers = []
    station.attach(self=station, customer=customer)
    # create order: pass customer's attributes, create route, schedule, delivery transport, driver
    transport = station.create_transport(self=station, customer=customer)
    route = create_route(origin=customer.point_A, destination=customer.point_B)
    driver.deliver()
    if driver.delivery_status:
        station.notify(self=station, customer=customer)

    # when order is completed, notify customer (change satisfaction to True)
    return [customer, transport]
