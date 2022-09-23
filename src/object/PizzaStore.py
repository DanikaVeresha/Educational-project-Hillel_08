import random


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(BaseClass, metaclass=Singleton):
    pass


class PizzaStore:
    '''описание пиццирии'''
    def __init__(self, pizzas: list, amount_check):
        '''свойства пиццирии'''
        self.pizzas = pizzas
        self.amount_check = amount_check
        self.sum = (lambda a: a.pizza.price * self.amount_check)  #переспросить верно ли это
        self.pizzas_less = filter(lambda a: a.pizza.price < 150, self.pizzas)
        self.pizzas_more = filter(lambda a: a.pizza.price > 150, self.pizzas)
        self.pizzas_is = filter(lambda a: a.pizza.price == 150, self.pizzas)

    def random_pizzas(self):
        '''cуть заказа клиента'''
        self.amount_check = random.randint(1, 3)
        return f'\n Check total: {self.sum} UAH'

    def __str__(self):
        '''список наших пицц, по ценовой категории с полным описанием пицци'''
        return f'\n The price of pizza is less than 150 UAH: {self.pizzas_less}' \
               f'\n The price of pizza is more than 150 UAH: {self.pizzas_more}' \
               f'\n The price of pizza is 150 UAH: {self.pizzas_is}'








