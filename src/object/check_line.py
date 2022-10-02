import random


class CheckLine:
    def __init__(self, date, month, number_check):
        self.date = date
        self.month = month
        self.nc = number_check

    def dec(self, func):
        def inner():
            print('----------------------------------------------------------------')
            func()
            self.date = random.randint(1, 31)
            self.month = random.randint(1, 12)
            self.number_check = random.randint(1, 100)
            print(f'data:_{self.date}/{self.month}/2022_, check_№:_{self.nc}_\n'
                  f'You were served by: - cashier:Veresha_Dasha')
            print('----------------------------------------------------------------')

        return inner


my_dec = CheckLine
my_dec.dec()

#верно ли этот файл я сделала?



