import random
from object.Pizza import Pizza


class Order(Pizza):
    '''описание чека'''
    def __init__(self, number, date, month):
        '''свойства чека'''
        super().__init__(idx, name, price, description)
        self.number = number
        self.date = date
        self.month = month
        
    def __str__(self):
        '''суть чека'''
        self.number = random.randint(1, 100)
        self.date = random.randint(1, 31)
        self.month = random.randint(1, 12)
        return f'\n ----------------------------------------------------------------' \
               f'\n data:_{self.date}/{self.month}/2022_, check_№:_{self.number}' \
               f'\n You were served by: - cashier:Veresha_Dasha' \
               f'\n ----------------------------------------------------------------'




