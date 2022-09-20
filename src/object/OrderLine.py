import random
from object.Pizza import Pizza


class OrderLine(Pizza):
    '''описание строки чека'''
    def __init__(self, pizza, amount):
        '''свойства строки чека'''
        super().__init__(idx, name, price, description)
        self.pizza = pizza
        self.amount = amount
        self.sum = 0


    def __str__(self):
        '''вывод на экран строки чека'''
        self.amount = random.randint(1, 6)
        self.pizza = random.sample(pizzas, self.amount)
        for item in self.pizza:
            n = random.randint(1, 3)
            self.sum += n * item.price
            return f'\n Number of pizzas in the order: {self.amount}'\
                   f'\n Pizza: {self.pizza}' \
                   f'\n pizza name: {item.name}' \
                   f'\n price of one pizza: {item.price} UAH' \
                   f'\n amount: {n}' \
                   f'\n Order price: {self.sum} UAH'













