import random


class OrderLine:
    '''описание строки чека'''
    def __init__(self, pizza, amount):
        '''свойства строки чека'''
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
            return f'Number of pizzas in the order: {self.amount}\n' \
                   f'Pizza: {self.pizza}\n' \
                   f'pizza name: {item.name}\n' \
                   f'price of one pizza: {item.price} UAH\n' \
                   f'amount: {n}\n' \
                   f'Order price: {self.sum} UAH'













