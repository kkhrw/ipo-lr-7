#Короленко
#Вариант 2
import json
operations = 0 #Счётчик выполненных операций
while True:
    print("\n======= МЕНЮ =======")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю id")
    print("3. Добавить запись")
    print("4. Удалить запись по id")
    print("5. Выйти из программы")
    print("====================")
    choice = input("Выберите пункт меню: ").strip()

    #Загружаем файл
    with open("flowers.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    #1.Вывести все записи
    if choice == "1":
        print("\n===== ВСЕ ЗАПИСИ =====") #Выводим меню 1
        for i, item in enumerate(data): #Перебираем элементы файла
            print(f"[{i}] id: {item[id]}, name: {item['name']}, "
                  f"latin_name: {item['latin_name']}, "
                  f"is_red_book_flower: {item['is_red_book_flower']}, "
                  f"price: {item['price']}")
        operations += 1 #считаем за операцию

    #2.Вывести запись по id
    elif choice == "2":
        try: #Выводим меню 2 и заправшиваем данные у пользователя
            find_id = int(input("Введите id: "))
        except:
            print("Некорректный id.") #Если id не находиться, выводим ошибку
            continue
        found = False
        for index, item in enumerate(data): #Перебираем файл в поиске элемента с нужным id
            if item["id"] == find_id:
                print("\n===== НАЙДЕНО =====")
                print(f"Позиция: {index}")
                print(f"id: {item['id']}")
                print(f"name: {item['name']}")
                print(f"latin_name: {item['latin_name']}")
                print(f"is_red_book_flower: {item['is_red_book_flower']}")
                print(f"price: {item['price']}")
                found = True
                break
        if not found:
            print("Запись не найдена!") #Если запись не находиться, выводим ошибку
        operations += 1 #считаем за операцию

    #3.Добавить запись
    elif choice == "3":
        try: #Выводим меню 3 и заправшиваем данные у пользователя
            new_id = int(input("id: "))
            new_name = input("Название: ")
            new_latin = input("Латинское название: ")
            new_redbook = input("Краснокнижный? (true/false): ").lower() == "true"
            new_price = float(input("Цена: "))
        except:
            print("Ошибка ввода данных!")
            continue
        data.append({  #Записываем данные в файл
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin,
            "is_red_book_flower": new_redbook,
            "price": new_price
        })
        with open("flowers.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        print("Запись добавлена.")
        operations += 1 #считаем за операцию


    #4.Удалить запись по id
    elif choice == "4":
        try: #Выводим меню 4 и заправшиваем данные у пользователя
            del_id = int(input("Введите id для удаления: "))
        except:
            print("Некорректный id!")
            continue
        removed = False
        for i in data:
            if i["id"] == del_id: #Если запись найдена по id, удаляем её
                data.remove(item)
                removed = True
                break
        if removed:
            with open("flowers.json", "w", encoding="utf-8") as f:
                json.dump(data, f) #Сохраняем изменения в файл
            print("Запись удалена.")
        else:
            print("Запись не найдена!")
        operations += 1 #считаем за операцию

    #5.Выход
    elif choice == "5": #Выводим меню 5
        print("\n===================================")
        print("Вы завершили программу.")
        print("Количество операций:", operations)
        print("===================================")
        break
    else:
        print("Неверный пункт меню!")
