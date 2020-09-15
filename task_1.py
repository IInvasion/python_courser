"""First practice task for sixth lesson."""

import sys
import time


class TrafficLight:
    """TrafficLight."""
    __color = 'red'

    def running(self, switches):
        """Switch light."""
        counter = 0
        while counter < switches:
            if self.__color == 'red':
                print('Traffic light is red!')
                time.sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print('Traffic light is yellow!')
                time.sleep(2)
                self.__color = 'green'
            else:
                print('Traffic light is green!')
                time.sleep(5)
                self.__color = 'red'
            counter += 1
        return True


def _main():
    """Entry point."""
    light = TrafficLight()
    light.running(15)


if __name__ == '__main__':
    sys.exit(_main())
