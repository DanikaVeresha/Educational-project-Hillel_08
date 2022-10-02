import random
from object.Pizza import Pizza


class OrderLine:
    '''атрибуты строки чека'''
    def __init__(self, pizza: Pizza, amount):
        '''свойства строки чека'''
        self.pizza = pizza
        self.amount = amount

    def random_types_of_pizzas(self):
        '''суть заказа'''
        self.amount = random.randint(1, 6)

    def __str__(self):
        return f'\n Pizza name: {self.pizza}'\
               f'\n Amount: {self.amount}'














