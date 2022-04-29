from abc import ABC


class Vehicle(ABC):
    def __init__(self,weight = 0,started = 0,fuel = 0,fuel_consumption = 0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_weight(self):
        pass

    def set_fuel(self):
        pass

    def set_fuel_consumption(self):
        pass

    def start(self):
        pass
