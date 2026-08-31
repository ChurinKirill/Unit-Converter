from abc import ABC, abstractmethod
from Units import *

class Converter(ABC):

    @abstractmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        pass

class LengthConverter(Converter):

    def convert(value: float, from_unit: str, to_unit: str) -> float:
        # переводим в метры
        match from_unit:
            case Length.meters:
                pass
            case Length.kilometers:
                value *= 1000
            case Length.foots:
                value /= 3.281
            case Length.miles:
                value *= 1609
            case Length.inches:
                value /= 39.37
            case _:
                return 0

        result = 0.0

        match to_unit:
            case Length.meters:
                result = value
            case Length.inches:
                result = value * 39.37
            case Length.miles:
                result = value / 1609
            case Length.foots:
                result = value * 3.281
            case Length.kilometers:
                result = value * 1000
            case _:
                return 0

        return result

class WeightConverter(Converter):

    def convert(value: float, from_unit: str, to_unit: str) -> float:
        # переводим в килограммы
        match from_unit:
            case Weight.kilograms:
                pass
            case Weight.grams:
                value /= 1000
            case Weight.milligrams:
                value /= 1000000
            case Weight.ounces:
                value /= 35.274
            case Weight.pounds:
                value /= 2.205
            case _:
                return 0

        result = 0.0

        match to_unit:
            case Weight.kilograms:
                result = value
            case Weight.pounds:
                result = value * 2.205
            case Weight.ounces:
                result = value * 35.274
            case Weight.milligrams:
                result = value * 1000000
            case Weight.grams:
                result = value * 1000
            case _:
                return 0

        return result
            
class TemperatureConverter(Converter):

    def convert(value: float, from_unit: str, to_unit: str) -> float:
        # переводим в Кельвины
        match from_unit:
            case Temperature.Kelvin:
                pass
            case Temperature.Celsius:
                value += 273
            case Temperature.Farenheit:
                value = (value - 32) * 5 / 9 + 273
            case _:
                return 0

        result = 0.0

        match to_unit:
            case Temperature.Kelvin:
                result = value
            case Temperature.Celsius:
                result = value - 273
            case Temperature.Farenheit:
                result = (value - 273) * 9 / 5 + 32
            case _:
                return 0

        return result
