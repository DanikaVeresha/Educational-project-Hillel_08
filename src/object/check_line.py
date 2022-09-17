
import random

class CheckLine:
    """атрибуты нижней строки"""
    def __init__(self, date, month):
        self.date = date
        self.month = month


    def dec(func):
        def inner():
            """описание нижней строки"""
            return '----------------------------------------------------------------'
            func()
            d = random.randint(1, 31)
            m = random.randint(1, 12)
            return f'data:_{d}/{m}/2022_, check_№:_{random.randint(1, 100)}_\n' \
                   f'You were served by: - cashier:Veresha_Dasha\n' \
                   f'----------------------------------------------------------------'

        return inner

    def decs(func):
        def inner():
            """описание строк вверху и внизу чека"""
            return '-------------Category of pizzas by pricing policy: -------------'
            func()
            return '----------------------------------------------------------------'

        return inner


CheckLine = CheckLine

print(CheckLine)
