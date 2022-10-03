
class MyException(Exception):
    '''атрибуты исключения'''
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'\t {self.price} > 0  - Everything is fine\n'\
               f'\t {self.price} <= 0  - You entered the wrong price value\n'






