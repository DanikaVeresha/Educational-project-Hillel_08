import random
from unittest import case
from collections import namedtuple

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
    print('Hello. 0 - Exit, 1 - print all pizzas')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            for Pizza in pizzas:
                print(Pizza)
        case '2':
            order = random.randint(1, 6)
            print(order)
        case '3':
            chek_1 = random.sample(pizzas, order)
            print(f"chek_1:{chek_1}")
            for Pizza in chek_1:
                print(Pizza, random.randint(1, 3))
        case '4':
            pizzas_1 = [Pizza for Pizza in pizzas if Pizza.price < 150]
            print(f'the price of pizza is less than 150 UAH:{pizzas_1}')
            pizzas_2 = [Pizza for Pizza in pizzas if Pizza.price > 150]
            print(f'the price of pizza is more than 150 UAH:{pizzas_2}')
            pizzas_3 = [Pizza for Pizza in pizzas if Pizza.price == 150]
            print(f'the price of pizza is 150 UAH:{pizzas_3}')
        case _:
            print('Wrong choise! Try again')

print('Bay') #Трішки щось не дуже гарно виходить к консолі(вид) та якщо можна ще допрацюю,
# почитаю завтра всі документи що Ви скинули
#захотілося відразу після заняття зробити домашку, перевірити себе як я зрозуміла лекцію)

