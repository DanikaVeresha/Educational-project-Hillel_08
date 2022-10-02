import random


class Check:
    '''описание чека'''
    def __init__(self, check_number, date, check_line: list):
        '''свойства чека'''
        self.check_number = check_number
        self.date = date
        self.check_line = check_line

    def receipt_details(self):
        '''суть чека'''
        self.check_number = random.randint(1, 100)
        self.date = random.randint(1, 31)

    def __str__(self):
        return f'\n ----------------------------------------------------------------' \
               f'\n Check_№:_{self.check_number}, date: _{self.date}/_08_/2022_' \
               f'\n Your order: {self.check_line}' \
               f'\n You were served by: - cashier: Veresha_Dasha' \
               f'\n ----------------------------------------------------------------'






