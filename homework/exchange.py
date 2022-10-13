from homework.read_remains_file import *


class Exchange:
    def __init__(self, course, course_ex, request):
        self.course = course
        self.request = request
        self.course_ex = course_ex

    def operationUAH(self):
        try:
            self.request = int(input('Amount in UAH: '))
            if self.request > 0:
                self.course_ex = courseUSD
                for item in self.course_ex:
                    result = self.request / item.rate
                    result1 = 1 / item.rate
                    if item.available >= result:
                        return f'UAH conversion: {round(result, 4)} | RATE: {round(result1, 6)}\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {result} USD\n' \
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
                self.course_ex = courseUAH
                for item in self.course_ex:
                    result = self.request * item.rate
                    result1 = 1 * item.rate
                    if item.available >= result:
                        return f'UAH conversion: {result} | RATE: {result1}\n'
                    else:
                        return f'Sorry, error.The currency balance is not enough\n' \
                               f'To complete the transaction, you must: {result} UAH\n' \
                               f'Available balance: {item.available} UAH\n'
            else:
                return f'Your exchange request:{self.request} is not correct'
        except ValueError:
            return f'Your exchange request is not correct'
        finally:
            print('Verification done')

    def __str__(self):
        txt = courseUAH
        txt += courseUSD
        txt += courseBCH
        txt = f' \t Course pairs list: {self.course}\n'
        for item in self.course_ex:
            txt += f'Course:{item.course} \t Rate:{item.rate} \t Available:{item.available}\n' \
                   f'Request: {self.request}\n' \
                   f'Exchange result: {self.course_ex}\n'
        txt = f'{self.course_ex}\n'

        return txt


