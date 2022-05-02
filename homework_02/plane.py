"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self,value_number: int):
        new_load_cargo_value = self.cargo + value_number
        if new_load_cargo_value > self.max_cargo:
            raise CargoOverload('it seems that it"s overload')
        self.cargo += new_load_cargo_value

    def remove_all_cargo(self):
        cargo_before_removing = self.cargo
        self.cargo = 0
        return cargo_before_removing
