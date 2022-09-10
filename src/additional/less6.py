li1 = {1, 2, 3, 4, 5, 6, 7}
li2 = {1, 2, 3, 4}

li1.difference_update(li2)
print(li1)
li2.difference_update(li1)
print(li2)

li1.discard(3)
print(li1)

li1.intersection_update(li2)
print(li1)

li3 = li1.isdisjoint(li2)
print(li3)

li3 = li1.issubset(li2)
print(li3) # Пoчему мне возращает Folse

li3 = li1.issuperset(li2)
print(li3)

li3 = li1.symmetric_difference(li2)
print(li3)

li1.symmetric_difference_update(li2)
print(li1)

li3 = li1.union(li2)
print(li3) #Не совсем понимаю что такое дубликаты в этом наборе