import random


class Order:
    '''описание чека'''
    def __init__(self, number, date, month):
        '''свойства чека'''
        self.number = number
        self.date = date
        self.month = month
        
    def decorator(self):
        def inner():
                print('----------------------------------------------------------------')
                self.number = random.randint(1, 100)
                self.date = random.randint(1, 31)
                self.month = random.randint(1, 12)
                print(f'data:_{self.date}/{self.month}/2022_, check_№:_{self.number}_\n'
                      f'You were served by: - cashier:Veresha_Dasha')
                print('----------------------------------------------------------------')

            return inner

