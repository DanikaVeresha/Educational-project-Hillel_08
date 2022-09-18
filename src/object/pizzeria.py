from object.pizza import Pizza


class Pizzeria:
    def __init__(self, up_to_150_UAH, more_than_150_UAH, equal_to_150_UAH):
        self.up = up_to_150_UAH
        self.more = more_than_150_UAH
        self.equal = equal_to_150_UAH

    def decs(self, func):
        def inner():
            print('-------------Category of pizzas by pricing policy: -------------')
            func()
            print('----------------------------------------------------------------')

        return inner

    @decs
    def list_pizzas(self):
        self.up = filter(lambda item: self.price < 150, pizzas)
        for item in self.up:
            print(f'the price of pizza is less than 150 UAH: {self.up}')
        self.more = filter(lambda item: self.price < 150, pizzas)
        for item in self.more:
            print(f'the price of pizza is more than 150 UAH: {self.more}')
        self.equal = filter(lambda item: self.price < 150, pizzas)
        for item in self.equal:
            print(f'the price of pizza is 150 UAH: {self.equal}')


my_pizza = Pizza
my_pizza.pizza_description()

#верно ли этот файл я сделала?

