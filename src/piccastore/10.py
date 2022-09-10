import random
from collections import namedtuple

Pizza = namedtuple('Pizza', ['idx', 'name', 'price', 'description'])


def pizzas_list():
    for item in Pizzas:
        print(f'{item.idx}, {item.name}\n'
              f' description: {item.description}\n'
              f' price: {item.price} UAH')


def dec(func):
    def inner():
        print('----------------------------------------------------------------')
        func()
        print(f'data_____, check_№:_{random.randint(1, 100)}_\n'
              f'You were served by: cashier - Veresha_Dasha')
        print('----------------------------------------------------------------')
    return inner


def decs(func):
    def inner():
        print('-------------Category of pizzas by pricing policy: -------------')
        func()
        print('----------------------------------------------------------------')
    return inner


@dec
def check():
    order = random.randint(1, 6)
    print(order)
    check = random.sample(Pizzas, order)
    for item in check:
        print(f'pizza: {item.name}\n'
              f'price of one pizza: {item.price} UAH\n'
              f'amount: {random.randint(1, 3)}')


@decs
def pizza_price_range():
    pizzas_1 = filter(lambda item: item.price < 150, Pizzas)
    for item in pizzas_1:
        print(f'the price of pizza is less than 150 UAH: {item.name}')
    pizzas_2 = filter(lambda item: item.price > 150, Pizzas)
    for item in pizzas_2:
        print(f'the price of pizza is more than 150 UAH: {item.name}')
    pizzas_3 = filter(lambda item: item.price == 150, Pizzas)
    for item in pizzas_3:
        print(f'the price of pizza is 150 UAH: {item.name}')


Pizzas = [
    Pizza(1, 'Hawaiian', 100, 'Chicken + pineapple + bakery + mozzarella + sauce'),
    Pizza(2, 'Carbonara', 110, 'Bacon + tavern + bakery + marinated + olives + mozzarella'),
    Pizza(3, 'M`yasna', 120, 'Bacon + salami + tomato + mozzarella'),
    Pizza(4, 'Margarita', 130, 'Tomato + mozzarella + sauce + salami'),
    Pizza(5, 'Mislivska', 140, 'Hunting sausages + salami + salted cucumber + garlic'),
    Pizza(6, 'Vegetable teriyaki', 150, 'Tomato + mushrooms + bell pepper + pickles'),
    Pizza(7, 'Pepperoni', 160, 'Pepperoni + italian herbs + mozzarella + signature sauce'),
    Pizza(8, 'Francesca', 170, 'Bacon + salami + mushrooms + tomato + olives + mozzarella'),
    Pizza(9, 'Four cheeses', 180, 'Dor bleu cheese + gouda cheese + cream cheese + mozzarella'),
    Pizza(10, 'Sharp', 200, 'Salami + tomatoes + bell pepper + green beans + sauce')
]

while True:
    print('Hello. 0 - Exit, 1 - all pizzas(), 2 - order, 3 - pizza_price_range')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            pizzas_list()
        case '2':
            check()
        case '3':
            pizza_price_range()
        case _:
            print('Wrong choise! Try again')

print('Bay')






