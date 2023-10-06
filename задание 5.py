d = {'Ожерелье': ['золото', 56, 12], 'Серьги': ['серебро', 37 , 3],
     'Кольцо': ['золото', 45 , 7], 'Браслет': ['золото', 64 , 8]}
while True:
    print("1. Просмотр описания ", '\n',
          "2. Просмотр цены ", '\n',
          "3. Просмотр количества", '\n',
          "4. Всю информацию", '\n',
          "5. Покупка", '\n',
          "6. До свидания")
    while True:
        try:
            a = int(input("Выберите операцию: "))
            break
        except ValueError:
            print("Ошибка")
    if a == 1:
        while True:
            name = input("Введите название изделия: ")
            name=name.title()
            if name.isalpha():
                break
            else:
                print("Вы ввели не букву")
        if name in d:
            f = d[name][0]
            print(name, ":", f)
        else:
            print("Изделие не найдено")
    elif a == 2:
        while True:
            name = input("Введите название изделия: ")
            name = name.title()
            if name.isalpha():
                break
            else:
                print("Вы ввели не букву")
        if name in d:
            price = d[name][1]
            print(name, ":", price)
        else:
            print("Изделие не найдено")
    elif a == 3:
        while True:
            name = input("Введите название изделия: ")
            name = name.title()
            if name.isalpha():
                break
            else:
                print("Вы ввели не букву")
        if name in d:
            count = d[name][2]
            print(name, ":", count)
        else:
            print("Изделие не найдено")
    elif a == 4:
        print("Вся информация об изделиях:")
        for name, info in d.items():
            print("Название: ", name)
            print("Описание: ", info[0])
            print("Цена: ", info[1])
            print("Количество: ", info[2], '\n')
    elif a == 5:
        t_price = 0
        n = []
        while True:
            while True:
                name = input("Введите название изделия: ")
                name = name.title()
                if name.isalpha():
                    break
                else:
                    print("Вы ввели не букву")
            if name not in d:
                print("Изделие не найдено")
                continue
            else:
                n.append(name)
            while True:
                try:
                    count = int(input("Введите количество: "))
                    break
                except ValueError:
                    print("Ошибка")
            if count > d[name][2]:
                print("Недостаточно товара")
                n.remove(name)
            else:
                n.append(count)
                price = d[name][1]
                t_price += price*count
                d[name][2] -= count
            m = input("Хотите выйти? (да/нет)")
            if m == 'да':
                break
        print("-------Ваш чек-------")
        print(n)
        print("-----Общая стоимость покупки: ", t_price)
        print("Осталось в магзине:")
        for name, info in d.items():
            print("Название: ", name)
            print("Описание: ", info[0])
            print("Цена: ", info[1])
            print("Количество: ", info[2], '\n')
    elif a == 6:
        break




