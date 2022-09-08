import random
from unittest import case
from collections import namedtuple
from functools import reduce

Pizza = namedtuple('Pizza', ['idx', 'name', 'price', 'description'])

def pizzas():
    for item in Pizzas:
        print(item.idx, item.name)
def chek():
    chek = random.sample(Pizzas, order)
    for item in chek:
        print(f"Chek:{item}")
    for item in chek:
        print(item, random.randint(1, 3))
def decorator(func):
    def inner():
        print('----------')
        func()
        print('data_____, chek_№__,You were served by: cashier - Veresha_Dasha')
    return inner
chek = decorator(chek)
def pizza_price_range():
    pizzas_1 = filter(lambda item: item.price < 150, Pizzas)
    for item in pizzas_1:
        print(f'the price of pizza is less than 150 UAH:{item.name}')
    pizzas_2 = filter(lambda item: item.price > 150, Pizzas)
    for item in pizzas_2:
        print(f'the price of pizza is more than 150 UAH:{item.name}')
    pizzas_3 = filter(lambda item: item.price == 150, Pizzas)
    for item in pizzas_3:
        print(f'the price of pizza is 150 UAH:{item.name}')


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
    print('Hello. 0 - Exit, 1 - all pizzas()')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            pizzas()
        case '2':
            order = random.randint(1, 6)
            print(order)
        case '3':
            chek()
        case '4':
            pizza_price_range()
        case _:
            print('Wrong choise! Try again')

print('Bay')