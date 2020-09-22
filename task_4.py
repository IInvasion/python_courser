"""Eight lesson fourth, fifth and sixth practice tasks."""

import sys


_EQUIPMENT = ['printer', 'scanner', 'xerox']


def move_from_storehouse(name, store_house):
    """Move office quipment from store house to department."""
    try:
        number = input(f'Enter number of {name} to move from store house to department: ')
        if int(number) > store_house.storage[name]:
            raise MoveFromStoreHouseError('Should be not greater than exists in store house.')
        store_house.to_department(name, int(number))
    except MoveFromStoreHouseError as err:
        print(err)
    except ValueError:
        print('Should be an integer')


class NotOfficeEquipmentError(Exception):
    """Is office equipment."""

    def __init__(self, text):
        """Constructor."""
        self.text = text


class MoveFromStoreHouseError(Exception):
    """Validate movement to department."""

    def __init__(self, text):
        """Constructor."""
        self.text = text


class StoreHouse:
    """StoreHouse."""

    def __init__(self, name):
        """Contructor."""
        self.storage = dict(printers=0, scanners=0, xeroxs=0)
        self.units = dict(printers=list(), scanners=list(), xeroxs=list())
        self.name = name

    def take_unit(self, unit):
        """Take unit."""
        if str(unit) in _EQUIPMENT:
            self.storage[str(unit) + 's'] += 1
            self.units[str(unit) + 's'].append(unit)
            unit.in_storage = True

    def to_department(self, name, number):
        """Move to department."""
        for element in self.units[name]:
            self.units[name].remove(element)
            element.in_storage = False
            element.in_department = True
            self.storage[name] -= number

    def __str__(self):
        """Cast to string."""
        string = f"Printers on storage - {self.storage['printers']}\n" + \
                 f"Scanners on storage - {self.storage['scanners']}\n" + \
                 f"Xeroxs on storage - {self.storage['xeroxs']}\n"
        string += 'Printers: '
        for element in self.units['printers']:
            string += str(element) + ' - ' + element._model + ', '
        string += '\nScanners: '
        for element in self.units['scanners']:
            string += str(element) + ' - ' + element._model + ', '
        string += '\nXeroxs: '
        for element in self.units['printers']:
            string += str(element) + ' - ' + element._model + ', '

        return string

class OfficeEquipment:
    """Base class for office quipment."""

    id_number = 0

    def __init__(self, model):
        """Constructor."""
        self._model = model
        self.in_storage = False
        self.in_department = False
        OfficeEquipment.id_number += 1
        self._id = OfficeEquipment.id_number

    def get_model(self):
        """Get model."""
        return self._model


class Printer(OfficeEquipment):
    """Printer."""

    def to_print(self):
        """Print document."""
        print(f'Printer {self._model} prints a document.')

    def __str__(self):
        """Cast to string."""
        return 'printer'


class Scanner(OfficeEquipment):
    """Scanner."""

    def to_scan(self):
        """Scan document."""
        print(f'Scanner {self._model} scans a document.')

    def __str__(self):
        """Cast to string."""
        return 'scanner'


class Xerox(OfficeEquipment):
    """Xerox."""

    def to_copy(self):
        """Copy document."""
        print(f'Xerox {self._model} scans a document.')

    def __str__(self):
        """Cast to string."""
        return 'xerox'


def _main():
    """Entry point."""
    store_house = StoreHouse('First storage')
    while True:
        try:
            item = input('Enter office equipment name or q for quit: ')
            if item == 'q':
                break
            if item not in _EQUIPMENT:
                raise NotOfficeEquipmentError(f'Should enter one of {_EQUIPMENT}')
            model = input(f'Enter {item} model: ')
            if item == 'printer':
                store_house.take_unit(Printer(model))
            elif item == 'scanner':
                store_house.take_unit(Scanner(model))
            elif item == 'xerox':
                store_house.take_unit(Xerox(model))
        except NotOfficeEquipmentError as err:
            print(err)
    print(store_house)
    print('How much scanners move to department?')
    if store_house.storage['printers'] > 0:
        move_from_storehouse('printers', store_house)
    if store_house.storage['scanners'] > 0:
        move_from_storehouse('scanners', store_house)
    if store_house.storage['xeroxs'] > 0:
        move_from_storehouse('xeroxs', store_house)
    print(store_house)

if __name__ == '__main__':
    sys.exit(_main())
