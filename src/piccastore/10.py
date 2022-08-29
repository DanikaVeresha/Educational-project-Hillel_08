import random
from itertools import count


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
a = random.randint(1, 6)
print(a)
chek_1 = random.sample(pizzas, a)
print(chek_1)
for i in chek_1:
    print(i)

    i = random.randint(1, 3)
    print(i)


