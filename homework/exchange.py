from homework.read_remains_file import *


class Exchange:
    def __init__(self, course_ex, request):
        self.request = request
        self.course_ex = course_ex

    def operationUAH(self):
        try:
            self.request = int(input('Amount in UAH: '))
            if self.request > 0:
                value = courseUSD
                for item in value:
                    self.course_ex = self.request / item.rate
                    result1 = 1 / item.rate
                    if item.available >= self.course_ex:
                        return f'UAH conversion: {round(self.course_ex, 4)} | RATE: {round(result1, 6)}\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {self.course_ex} USD\n' \
                               f'Available balance: {item.available} USD\n'
            else:
                return f'Your exchange request:{self.request} is not correct'
        except ValueError:
            return 'Your exchange request is not correct'
        finally:
            print('Verification done')

    def operationUSD(self):
        try:
            self.request = int(input('Amount in UAH: '))
            if self.request > 0:
                value = courseUAH
                for item in value:
                    self.course_ex = self.request * item.rate
                    result1 = 1 * item.rate
                    if item.available >= self.course_ex:
                        return f'USD conversion: {self.course_ex} | RATE: {result1}\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {self.course_ex} UAH\n' \
                               f'Available balance: {item.available} UAH\n'
            else:
                return f'Your exchange request:{self.request} is not correct'
        except ValueError:
            return f'Your exchange request is not correct'
        finally:
            print('Verification done')

    def __str__(self):
        return f'UAH conversion: {self.course_ex} UAH\n' \
               f'USD conversion: {self.course_ex} USD\n'









