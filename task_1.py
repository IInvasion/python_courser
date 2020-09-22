"""Eight lesson first practice task."""

import sys

_LONG_MONTHES = [1, 3, 5, 7, 8, 10, 12]


def month_day_validate(month_day, month_days):
    """Validate month day."""
    if month_day < 1 or month_day > month_days:
        return False

    return True


class Data:
    """Data tools."""

    def __init__(self, data):
        """Constructor."""
        self.data = data

    @staticmethod
    def _validate(day, month, year):
        """Validate."""
        try:
            month = int(month)
            day = int(day)
            year = int(year)
            if year < 0:
                return False
            if not month_day_validate(month, 12):
                return False
            if month in _LONG_MONTHES:
                if not month_day_validate(day, 31):
                    return False
            elif month == 2:
                if year % 4 == 0 and year % 400 != 0:
                    if not month_day_validate(day, 29):
                        return False
                else:
                    if not month_day_validate(day, 28):
                        return False
            else:
                if not month_day_validate(day, 30):
                    return False
            return True
        except ValueError:
            print('Day, month and year should be an integer.')

    @classmethod
    def to_number(cls, data):
        """Data to number."""
        day, month, year = data.split('-')
        days_number = 0
        if cls._validate(day, month, year):
            day, month, year = int(day), int(month), int(year)
            for i in range(month):
                if i+1 == month:
                    days_number += day
                else:
                    if i+1 in _LONG_MONTHES:
                        days_number += 31
                    elif i+1 == 2:
                        if year % 4 == 0 and year % 400 != 0:
                            days_number += 29
                        else:
                            days_number += 28
                    else:
                        days_number += 30

        return days_number


def _main():
    """Entry point."""
    data = '06-06-1990'
    obj = Data(data)
    result = Data.to_number(obj.data)
    print(result)


if __name__ == '__main__':
    sys.exit(_main())
