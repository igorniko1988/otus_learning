from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError(f'not enough fuel {self.fuel} to start')
        self.started = True

    def move(self,distance):
        fuel_to_reach_distance = self.fuel_consumption * distance
        if self.fuel < fuel_to_reach_distance:
            raise NotEnoughFuel('not enough fuel to reach distance')
        self.fuel -= fuel_to_reach_distance

