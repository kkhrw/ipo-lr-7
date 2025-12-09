# # Козлова 1 вариант
# import json
# import os
# print("start code ...")

# filename = "flowers.json"

# if os.path.exists(filename):
#     with open(filename, "r", encoding="utf-8") as f:
#         flowers = json.load(f)
# else:
#     flowers = []

# operation_count = 0

# while True:
#     print("\nМеню выбора:")
#     print("1. Вывести все записи")
#     print("2. Вывести запись по полю")
#     print("3. Добавить запись")
#     print("4. Удалить запись по полю")
#     print("5. Выйти из программы")
    
#     choice = input("Выберите один из пунктов (1-5): ").strip()
    
#     if choice == "1":
#         print("\n============== Все записи ==============")
#         if not flowers:
#             print("Нет записей.")
#         else:
#             for flower in flowers:
#                 is_red_book_flower  = "краснокнижный" if flower['is_red_book_flower'] else "не краснокнижный"
#                 print(f"ID: {flower['id']}")
#                 print(f"Общее название: {flower['name']}")
#                 print(f"Латинское название: {flower['latin_name']}")
#                 print(f"Красная книга: {is_red_book_flower}")
#                 print(f"Цена: {flower['price']}")
#                 print("-" * 40)
#         operation_count += 1

#     # elif choice == "2"
#         try:
#             target_id = int(input("Введите ID цветка: "))
#             found = False
#             for index, flower in enumerate(flowers):
#                 if flower["id"] == target_id:
#                     print(f"\n============== Найдено ==============")
#                     print(f"Позиция в списке: {index + 1}")
#                     is_red_book_flower = "краснокнижный" if flower["is_red_book_flower"] else "не краснокнижный"
#                     print(f"ID: {flower['id']}")
#                     print(f"Общее название: {flower['name']}")
#                     print(f"Латинское название: {flower['latin_name']}")
#                     print(f"Красная книга: {is_red_book_flower}")
#                     print(f"Цена: {flower['price']}")
#                     found = True
#                     break
#             if not found:
#                 print("\n============== Не найдено ===============")
#         except ValueError:
#             print("Некорректный ввод ID.")
#         operation_count += 1

#     elif choice == "3":
#         try:
#             new_id = max([s["id"] for s in flowers], default=0) + 1
#             name = input("Введите общее название цветка: ").strip()
#             latin_name = input("Введите научное название цветка: ").strip()
#             is_red_book_flower = input("Этот цветок в красной книге? (да/нет): ").strip().lower()
#             is_red_book_flower = True if is_red_book_flower in ("да", "yes", "y", "1") else False
#             price = float(input("Введите цену растения: "))
#             new_flower = {
#                 "id": new_id,
#                 "name": name,
#                 "latin_name": latin_name,
#                 "is_red_book_flower": is_red_book_flower,
#                 "price": price
#             }
#             flowers.append(new_flower)
#             with open(filename, "w", encoding="utf-8") as f:
#                 json.dump(flowers, f, ensure_ascii=False, indent=4)
#             print("Запись успешно добавлена.")
#         except ValueError:
#             print("Цена должна быть числом.")
#         operation_count += 1

#     elif choice == "4":
#         try:
#             target_id = int(input("Введите ID цветка для удаления: "))
#             initial_len = len(flowers)
#             flowers = [s for s in flowers if s["id"] != target_id]
#             if len(flowers) == initial_len:
#                 print("\n============== Не найдено ===============")
#             else:
#                 with open(filename, "w", encoding="utf-8") as f:
#                     json.dump(flowers, f, ensure_ascii=False, indent=4)
#                 print("Запись успешно удалена.")
#         except ValueError:
#             print("Некорректный ввод ID.")
#         operation_count += 1

#     elif choice == "5":
#         print(f"\nВыполнено операций: {operation_count}")
#         print("... end code")
#         break

#     else:
#         print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")
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
            print(f"[{i}] id: {item['id']}, name: {item['name']}, "
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