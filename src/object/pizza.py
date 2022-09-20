

class Pizza:
    '''описание пицци'''
    def __init__(self, idx, name, price, description):
        '''свойства пицци'''
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        '''вывод на экран ппицци'''
        return f'Pizza {self.idx}: {self.name}\n' \
               f'Description: {self.description}\n' \
               f'Price: {self.price} UAH'




