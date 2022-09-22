import random
from object.Pizza import Pizza


class OrderLine:
    '''атрибуты строки чека'''
    def __init__(self, pizza: Pizza, amount_for_check, amount_for_order):
        '''свойства строки чека'''
        self.pizza = pizza
        self.amount_for_check = amount_for_check
        self.amount_for_order = amount_for_order
        self.sum = self.amount_for_order * self.pizza.price

    def random_pizza(self):
        '''суть заказа'''
        self.amount_for_check = random.randint(1, 6)
        self.amount_for_order = random.randint(1, 3)

    def __str__(self):
        return f'\n Pizza name: {self.pizza}'\
               f'\n Amount: {self.amount_for_check}' \
               f'\n Total_for_order: {self.sum} UAH'














