while True:
    try:
        a=int(input("Введите натуральное число: "))
        original_a = a
        break
    except ValueError:
        print("Ошибка")
max_digit = 0
while a > 0:
    digit1 = a%10
    if digit1 > max_digit:
        max_digit = digit1
    a //= 10
print("Максимальная цифра:", max_digit)
# Последнюю цифру первого числа переносим во второе
n2 = 0
while original_a > 0:
    # находим остаток - последнюю цифру
    digit = original_a % 10
    # делим нацело - удаляем последнюю цифру
    original_a= original_a // 10
    # увеличиваем разрядность второго числа
    n2 = n2 * 10
    # добавляем очередную цифру
    n2 = n2 + digit
print('Число в обратном порядке:', n2)