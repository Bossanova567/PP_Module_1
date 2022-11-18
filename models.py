from typing import Optional, List
from uuid import UUID, uuid4
from abc import abstractmethod, ABC

from pydantic import BaseModel


class Route(BaseModel):
    point_A: str
    point_B: str
    distance: int
    travel_time: int


class TransportDepartment(ABC):
    @abstractmethod
    def prepare_transport(self, needed_load_weight):
        pass


class VanGarage(TransportDepartment):
    def prepare_transport(self, needed_load_weight: int):
        return Van(needed_load_weight)


class TruckGarage(TransportDepartment):
    def prepare_transport(self, needed_load_weight: int):
        return Truck(needed_load_weight)

    def prepare_transport(self, needed_load_weight: int, trailer_type: str):
        return Truck(needed_load_weight, trailer_type)


class Transport(ABC):
    load_weight: int


class Van(Transport):
    def __init__(self, needed_load_weight: int):
        self.load_weight = needed_load_weight


class Truck(Transport):
    def __init__(self, needed_load_weight: int, trailer_type: str):
        self.load_weight = needed_load_weight
        self.trailer_type = trailer_type


class Person(BaseModel, ABC):
    id: Optional[UUID] = uuid4()
    name: str

    @abstractmethod
    def update(self):
        pass


class Driver(Person):
    delivery_status: bool = False

    def update(self):
        pass

    def deliver(self):
        self.delivery_status = True


class Customer(Person):
    point_A: str
    point_B: str
    load_weight: int
    trailer_type: str
    satisfaction: bool = False

    def update(self):
        self.satisfaction = True


class Company(ABC):
    @abstractmethod
    def attach(self, customer: Customer):
        pass

    @abstractmethod
    def detach(self, customer: Customer):
        pass

    def notify(self, customer: Customer):
        pass


class Station(BaseModel, Company):
    customers: List[Customer]
    routes: List[Route]

    def attach(self, customer: Customer):
        if self.customers.count(customer) != 0:
            return f"{customer} is already subscribed"
        else:
            self.customers.append(customer)

    def detach(self, customer: Customer):
        if self.customers.count(customer) != 0:
            self.customers.remove(customer)
        else:
            return f"{customer} is not subscribed"

    def notify(self, customer: Customer):
        if self.customers.count(customer) != 0:
            if not customer.satisfaction:
                customer.update()
            else:
                raise Exception

    def create_transport(self, customer: Customer):
        if customer.load_weight < 1000:
            van_garage = VanGarage()
            return van_garage.prepare_transport(customer.load_weight)
        else:
            truck_garage = TruckGarage
            if customer.trailer_type:
                return truck_garage.prepare_transport(self=truck_garage,needed_load_weight=customer.load_weight, trailer_type=customer.trailer_type)
            return truck_garage.prepare_transport(customer.load_weight)
