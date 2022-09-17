
import random

class Check:
    """атрибуты чека"""
    def __init__(self, number_of_pizzas, random_pizzas, number_of_random_pizzas, check_amount):
        self.np = number_of_pizzas
        self.rp = random_pizzas
        self.nrp = number_of_random_pizzas
        self.ca = check_amount



    @dec
    def __str__(self)::
        order = random.randint(1, 6)
        return f'Number of pizzas in the order: {order}'
        check = random.sample(pizzas, order)
        sum = 0
        for item in check:
            n = random.randint(1, 3)
            return f'pizza name: {item.name}\n' \
                   f'price of one pizza: {item.price} UAH\n' \
                   f'amount: {n}'
            sum += n * item.price
        return f'Order price: {sum} UAH'


Check = Check

print(Check)