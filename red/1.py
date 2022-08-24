print(2*3, type(2*3))
result = ((3*3+8)/3)
print(result, type(result))
print(8//3, type(8//3))
print(8%3, type(8%3))
print(5**2, type(5**2))
print('hello' + 'world', type('hello' + 'world'))

str_1 = 'helloworlditsmedashaveresha'
str_2 = "HELLOWORLDITSMEDASHAVERESHA"
print(str_1, str_2)

str_2 = "HELLOWORLDITSMEDASHAVERESHA"
str = str_2[:10]
print(str)
str_1 = str_2[2:12]
print(str_1)
str_3 = str_2[-10:]
print(str_3)
str_4 = str_2[::-1]
print(str_4)
a = len(str_2)
print(a)
b = (list(enumerate(str_2)))
print(b)

a = input('a: ')
b = input('b: ')
c = a+b
print(c, type(c))