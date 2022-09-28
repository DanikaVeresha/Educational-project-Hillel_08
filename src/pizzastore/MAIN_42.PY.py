from object.PIZZALIST import pizzas
from object.PIZZASTORE import Pizzastore
from object.my_exception import MyException


def exs(ex):
    print(ex.filter_price())


def main(ps):

    while True:
        print('Hello. 0 - Exit, 1 - all pizzas(), 2 - order, 3 - pizza_price_range')
        c = input('Your choise: ')
        match c:
            case '0':
                break
            case '1':
                print(ps.pizzas)
            case '2':
                ps.add_random_check()
                print(ps.checks[-1])
            case '3':
                print(ps.pizzas_1)
                print(ps.pizzas_2)
                print(ps.pizzas_3)
            case _:
                print('Wrong choise! Try again')

        print('Bay')


if __name__ == '__main__':
    ps = Pizzastore(pizzas)
    ex = MyException(Exception)

