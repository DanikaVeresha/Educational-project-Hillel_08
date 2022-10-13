from homework.exchange import *
from homework.currency_pairs_list import *


def main(x):
    while True:
        print(f'Hello.\n'
              f'0 - STOP\n'
              f'1 - COURSE USD\n'
              f'2 - COURSE UAH\n'
              f'3 - COURSE BCH\n'
              f'4 - EXCHANGE UAH\n'
              f'5 -  EXCHANGE USD')
        client = input('Your choise: ')
        match client:
            case '0':
                break
            case '1':
                print(x.Course(courseUSD))
            case '2':
                print(x.Course(courseUAH))
            case '3':
                print(x.Course(courseBCH))
            case '4':
                x.operationUAH()
            case '5':
                x.operationUSD()
            case _:
                print('Wrong choice, look in the program menu "Exchanger"')

    print('SERVICE STOPPED')


if __name__ == '__main__':
    x = Exchange(courseUSD, courseUAH)
    d = Course(courseUSD, courseUAH, courseBCH)

