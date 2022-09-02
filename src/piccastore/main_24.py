import random

pizzas = [
    (1, 'Hawaiian', 100, 'Chicken + pineapple + bakery + mozzarella + sauce'),
    (2, 'Carbonara', 110, 'Bacon + tavern + bakery + marinated + olives + mozzarella'),
    (3, 'M`yasna', 120, 'Bacon + salami + tomato + mozzarella'),
    (4, 'Margarita', 130, 'Tomato + mozzarella + sauce + salami'),
    (5, 'Mislivska', 140, 'Hunting sausages + salami + salted cucumber + garlic'),
    (6, 'Vegetable teriyaki', 150, 'Tomato + mushrooms + bell pepper + pickles'),
    (7, 'Pepperoni', 160, 'Pepperoni + italian herbs + mozzarella + signature sauce'),
    (8, 'Francesca', 170, 'Bacon + salami + mushrooms + tomato + olives + mozzarella'),
    (9, 'Four cheeses', 180, 'Dor bleu cheese + gouda cheese + cream cheese + mozzarella'),
    (10, 'Sharp', 200, 'Salami + tomatoes + bell pepper + green beans + sauce')
]

while True:
    print('Hello. 0 - Exit, 1 - print all pizzas')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            for item in pizzas:
                print(item)
        case _:
            print('Wrong choise! Try again')
    order = random.randint(1, 6)
    print(order)
    chek_1 = random.sample(pizzas, order)
    print(f"chek_1:{chek_1}")
    for item in chek_1:
        print(item)
        item = random.randint(1, 3)
        print(item)
    pizzas_1 = [item for item in pizzas if item[2] < 150]
    print(f'the price of pizza is less than 150 UAH:{pizzas_1}')
    pizzas_2 = [item for item in pizzas if item[2] > 150]
    print(f'the price of pizza is more than 150 UAH:{pizzas_2}')
    pizzas_3 = [item for item in pizzas if item[2] == 150]
    print(f'the price of pizza is 150 UAH:{pizzas_3}')

print('Bay')

