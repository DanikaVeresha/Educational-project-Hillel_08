from object.PIZZALIST import pizzas


class Pizza:
    '''атрибуты пицци'''
    def __init__(self, idx, name, price, description):
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        '''пицца на екран'''
        for item in pizzas:
            return f'{item.idx}. {item.name}:\n' \
                   f'Описание пицци: {item.description}\n'












