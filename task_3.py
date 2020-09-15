"""Third practice task for sixth lesson."""

import sys


class Worker:
    """Worker."""

    def __init__(self, name, surname, wage, bonus):
        """Constructor."""
        self.name = name
        self.surname = surname
        self._income = dict(wage=wage, bonus=bonus)

    def get_income(self):
        """Get income dictionary."""
        return self._income


class Position(Worker):
    """Position."""

    def __init__(self, name, surname, wage, bonus, position):
        """Contructor."""
        super().__init__(name, surname, wage, bonus)
        self.position = position

    def get_full_name(self):
        """Get worker's full name."""
        return self.name + ' ' + self.surname

    def get_total_income(self):
        """Get worker's total income."""
        return self._income['wage'] + self._income['bonus']


def _main():
    """Entry point."""
    current_worker = Worker('Evgeny', 'Shevchenko', 100500, 42)
    worker_position = Position('Evgeny', 'Shevchenko', 100500, 42, 'QA-specialist')
    print(current_worker.get_income())
    print(current_worker.name + ' ' + current_worker.surname)
    print(worker_position.position)
    print(f"Worker's credentianls: {worker_position.get_full_name()}")
    print(f"Worker's total income: {worker_position.get_total_income()}")

if __name__ == '__main__':
    sys.exit(_main())
