from object.price import Price
from object.pizza import Pizza
from object.check_line import CheckLine
from object.check import Check


while True:
    print('Hello. 0 - Exit, 1 - all pizzas(), 2 - order, 3 - pizza_price_range')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            print(Pizza)
        case '2':
            print(CheckLine)
            print(Check)
        case '3':
            print(Price)
        case _:
            print('Wrong choise! Try again')

print('Bay')