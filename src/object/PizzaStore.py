

class PizzaStore:
    '''описание пиццирии'''
    def __init__(self, pizzas: list):
        '''свойства пиццирии'''
        self.pizzas = pizzas

    def pizza_price_range(self):
        self.pizzas = filter(lambda a: a.pizza.price < 150, self.pizzas)
        self.pizzas = filter(lambda a: a.pizza.price > 150, self.pizzas)
        self.pizzas = filter(lambda a: a.pizza.price == 150, self.pizzas)


    def __str__(self):
        '''список наших пицц, по ценовой категории с полным описанием пицци'''
        return f'\n The price of pizza is less than 150 UAH: {self.pizzas}' \
               f'\n The price of pizza is more than 150 UAH: {self.pizzas}' \
               f'\n The price of pizza is 150 UAH: {self.pizzas}'



#class Singleton(type):
#    _instances = {}
#
#    def __call__(cls, *args, **kwargs):
#        if cls not in cls._instances:
#            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#        return cls._instances[cls]


#class MyClass(BaseClass, metaclass=Singleton):
#    pass





