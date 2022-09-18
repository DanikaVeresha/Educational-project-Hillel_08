import random
from object.check_line import CheckLine


class Check:
    def __init__(self, number_of_pizzas, random_pizzas, number_of_random_pizzas, check_amount):
        self.number_of_pizzas = number_of_pizzas
        self.random_pizzas = random_pizzas
        self.number_of_random_pizzas = number_of_random_pizzas
        self.check_amount = check_amount
    @dec
    def my_order(self):
        order = random.randint(1, 6)
        print(f'Number of pizzas in the order: {order}')
        check = random.sample(pizzas, order)
        sum = 0
        for item in check:
            n = random.randint(1, 3)
            print(f'pizza name: {item.name}\n'
                  f'price of one pizza: {item.price} UAH\n'
                  f'amount: {n}')
            sum += n * item.price
        print(f'Order price: {sum} UAH')


line = CheckLine
line.dec()




