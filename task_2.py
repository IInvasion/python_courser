"""Second practice task from seventh lesson."""

import sys
from abc import ABC, abstractmethod, abstractproperty

_CLOTHES = ['coat', 'suit']


class Clothes(ABC):
    """Abstract class."""
    @abstractmethod
    def evaluate_consumption(self):
        """Evaluate consumption."""

    @abstractproperty
    def clothes_type(self):
        """Clothes type."""


class GarmentFactory(Clothes):
    """Garment factory."""

    def __init__(self, clothes_type, size):
        """Constructor."""
        self.clothes_type = clothes_type
        self.size = size

    @property
    def clothes_type(self):
        """Property."""
        return self.__clothes_type

    @clothes_type.setter
    def clothes_type(self, clothes_type):
        """Setter."""
        if clothes_type not in _CLOTHES:
            self.__clothes_type = 'UndefinedClothes'
        else:
            self.__clothes_type = clothes_type

    def get_clothes_type(self):
        """Getter."""
        return self.clothes_type

    def evaluate_consumption(self):
        """Evaluate consumption."""
        if self.get_clothes_type() == 'coat':
            consumption = self.size / 6.5 + 0.5
        elif self.get_clothes_type() == 'suit':
            consumption = 2 * self.size + 0.3
        else:
            consumption = 'Cannot evaluate consumption for undefined clothes type'

        return consumption


def _main():
    """Entry point."""
    coat = GarmentFactory('coat', 10)
    suit = GarmentFactory('suit', 15)
    hat = GarmentFactory('hat', 25)
    print(coat.evaluate_consumption())
    print(suit.evaluate_consumption())
    print(hat.evaluate_consumption())


if __name__ == '__main__':
    sys.exit(_main())
