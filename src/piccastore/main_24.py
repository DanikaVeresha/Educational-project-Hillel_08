import random
from unittest import case
from collections import namedtuple

def Pizzas():
    for item in pizzas:
        print(item)
def Chek():
    Chek = random.sample(pizzas, order)
    for item in Chek:
        print(f"Chek:{item}")
    for item in Chek:
        print(item, random.randint(1, 3))
def Decorator(func):
    def inner():
        print('----------')
        func()
        print('data_____, chek_№__,You were served by: cashier - Veresha_Dasha')
    return inner
Chek = Decorator(Chek)
def Pizza_price_range():
    pizzas_1 = [item for item in pizzas if item.price < 150]
    for item in pizzas_1:
        print(f'the price of pizza is less than 150 UAH:{item}')
    pizzas_2 = [item for item in pizzas if item.price > 150]
    for item in pizzas_2:
        print(f'the price of pizza is more than 150 UAH:{item}')
    pizzas_3 = [item for item in pizzas if item.price == 150]
    for item in pizzas_3:
        print(f'the price of pizza is 150 UAH:{item}')

Pizza = namedtuple('Pizza', ['idx', 'name', 'price', 'description'])
pizzas = [
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
            Pizzas()
        case '2':
            order = random.randint(1, 6)
            print(order)
        case '3':
            Chek()
        case '4':
            Pizza_price_range()
        case _:
            print('Wrong choise! Try again')

print('Bay')