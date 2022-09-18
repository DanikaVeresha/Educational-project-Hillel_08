import random
from object.check_line import CheckLine


class Check:
    def __init__(self, number_of_pizzas, random_pizzas, number_of_random_pizzas, check_amount):
        self.np = number_of_pizzas
        self.rp = random_pizzas
        self.nrp = number_of_random_pizzas
        self.ca = check_amount
    @dec
    def my_order(self):
        self.np = random.randint(1, 6)
        print(f'Number of pizzas in the order: {self.np}')
        self.rp = random.sample(pizzas, self.np)
        self.ca = 0
        for item in self.rp:
            self.nrp = random.randint(1, 3)
            print(f'pizza name: {self.name}\n'
                  f'price of one pizza: {self.price} UAH\n'
                  f'amount: {self.nrp}')
            self.ca += self.nrp * item.price
        print(f'Order price: {self.ca} UAH')


my_dec = CheckLine
my_dec.dec()

#верно ли этот файл я сделала?




