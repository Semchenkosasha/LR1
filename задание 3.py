import random
p = 1
i = 1
k = 0
elements = []
while True:
    try:
        a = int(input("Введите количестно элементов: "))
        break
    except ValueError:
        print("Ошибка")
while i <= a:
    element = random.randrange(0, 10)
    elements.append(element)
    i += 1
print("Список: ", elements)
for i in range(len(elements)):
    if (i +1) % 2 == 1:
        p *= elements[i]
print("Произведение:", p)
m = max(elements)
elements.remove(m)
print("Новый список: ", elements)
sorted_elements = sorted(elements, reverse=True)
l = sorted_elements[:3]
print("Три наибольших элемента списка:", l)