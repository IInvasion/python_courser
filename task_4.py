"""Fourth practice task for sixth lesson."""

import sys


class Car:
    """Car."""

    def __init__(self, speed, color, name):
        """Constructor."""
        self._speed = speed
        self._color = color
        self._name = name

    def go(self):
        """Go."""
        print('Car run')

    def stop(self):
        """Stop."""
        print('Car stoped')

    def turn(self, direction):
        """Change direction."""
        print(f'Car new direction is {direction}')

    def show_speed(self):
        """Show speed."""
        print(f'Car speed equals {self._speed}')


class TownCar(Car):
    """Town car."""

    def __init__(self, speed, color, name):
        """Constructor."""
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        """Show speed."""
        if self._speed > 60:
            print(f'Car speed equals {self._speed} and exceeds maximum allowed speed for this car!')
        else:
            print(f'Car speed equals {self._speed}')


class WorkCar(Car):
    """Work car."""

    def __init__(self, speed, color, name):
        """Constructor."""
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        """Show speed."""
        if self._speed > 40:
            print(f'Car speed equals {self._speed} and exceeds maximum allowed speed for this car!')
        else:
            print(f'Car speed equals {self._speed}')


class SportCar(Car):
    """Sport car."""

    def __init__(self, speed, color, name):
        """Constructor."""
        super().__init__(speed, color, name)
        self.is_police = False


class PoliceCar(Car):
    """Police car."""

    def __init__(self, speed, color, name):
        """Constructor."""
        super().__init__(speed, color, name)
        self.is_police = True


def _main():
    """Entry point."""
    sport_car = SportCar(1200, 'red', 'ENZO')
    town_car = TownCar(60, 'green', 'Chevrolet')
    work_car = WorkCar(42, 'orange', 'KAMAZ')
    police_car = PoliceCar(2300, 'black', 'Dodge')
    sport_car.go()
    town_car.stop()
    work_car.turn('left')
    sport_car.show_speed()
    town_car.show_speed()
    work_car.show_speed()
    police_car.show_speed()
    print(work_car.is_police)
    print(town_car.is_police)
    print(sport_car.is_police)
    print(police_car.is_police)


if __name__ == '__main__':
    sys.exit(_main())
