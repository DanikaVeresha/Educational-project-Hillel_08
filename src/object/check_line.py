import random


class CheckLine:
    def __init__(self, date, month):
        self.date = date
        self.month = month

    def dec(self, func):
        def inner():
            print('----------------------------------------------------------------')
            func()
            d = random.randint(1, 31)
            m = random.randint(1, 12)
            print(f'data:_{d}/{m}/2022_, check_№:_{random.randint(1, 100)}_\n'
                  f'You were served by: - cashier:Veresha_Dasha')
            print('----------------------------------------------------------------')

        return inner



