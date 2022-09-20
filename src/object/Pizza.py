

class Pizza:
    '''описание пицци'''
    def __init__(self, idx, name, price, description):
        '''свойства пицци'''
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        '''вывод на экран пицци'''
        return f'\n Pizza: {self.idx}: {self.name}' \
               f'\n Description: {self.description}' \
               f'\n Price: {self.price} UAH'




