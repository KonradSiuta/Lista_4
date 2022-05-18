from abc import ABC, abstractmethod
import random


class Temperature(ABC):
    @abstractmethod
    def __init__(self, temperature) -> None:
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    def __str__(self) -> str:
        return f'{round(self.temperature,2)}º w skali {type(self).__name__}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.temperature})'

    def above_freezing(self) -> bool:
        return self.convert_to_celsius().temperature > 0

    @abstractmethod
    def convert_to_celsius(self):
        pass

    @abstractmethod
    def convert_to_fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_kelvin(self):
        pass

class Celsius(Temperature):
    def __init__(self, temperature) -> None:
        super().__init__(temperature)

    def convert_to_celsius(self):
        return self

    def convert_to_fahrenheit(self):
        return Fahrenheit(self.temperature * 1.8 + 32)

    def convert_to_kelvin(self):
        return Kelvin(self.temperature + 273.16)

class Fahrenheit(Temperature):
    def __init__(self, temperature) -> None:
        super().__init__(temperature)

    def convert_to_fahrenheit(self):
        return self

    def convert_to_celsius(self):
        return Celsius((self.temperature - 32) * 0.556)

    def convert_to_kelvin(self):
        return Kelvin((self.temperature + 459.67) * 5/9)

class Kelvin(Temperature):
    def __init__(self, temperature) -> None:
        super().__init__(temperature)

    def convert_to_kelvin(self):
        return self
    
    def convert_to_celsius(self):
        return Celsius(self.temperature - 273.16)

    def convert_to_fahrenheit(self):
        return Fahrenheit((self.temperature - 273.16) * 9/5 + 32)

if __name__ == "__main__":
    temperatures_list = []
    for i in range(4):
        temperatures_list.append(Celsius(random.randint(-273, 273)))
        temperatures_list.append(Fahrenheit(random.randint(-100, 100)))
        temperatures_list.append(Kelvin(random.randint(0, 500)))

    # for temperature in temperatures_list:
        # print(temperature, "powyzej zera" if temperature.above_freezing() else "")

    converted_to_celsius = [temp.convert_to_celsius() for temp in temperatures_list]
    converted_to_fahrenheit = [temp.convert_to_fahrenheit() for temp in temperatures_list]
    converted_to_kelvin = [temp.convert_to_kelvin() for temp in temperatures_list]

    for temperature in converted_to_celsius:
        if temperature.above_freezing():
            print(temperature)

    for temperature in converted_to_fahrenheit:
        if temperature.above_freezing():
            print(temperature)

    for temperature in converted_to_kelvin:
        if temperature.above_freezing():
            print(temperature)