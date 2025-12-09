import json
import os

# Загрузка данных из файла
def load_data():
    try:
        with open('flowers.json', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Ошибка: файл flowers.json не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка: файл flowers.json содержит некорректный JSON.")
        return None

# Сохранение данных в файл
def save_data(data):
    try:
        with open('flowers.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError:
        print("Ошибка при сохранении данных.")

# Вывод информации об одном цветке
def display_flower(flower):
    print(f"============ {flower['name']} ============")
    print(f'Номер цветка - {flower["id"]}, Латинское название - {flower["latin_name"]}')
    if flower["is_red_book_flower"]:
        print(f'{flower["name"]} является краснокнижным цветком')
    else:
        print(f'{flower["name"]} не является краснокнижным цветком')
    print(f'=============== Цена: {flower["price"]} ===============')
    print()

# Вывод всех записей
def display_all_flowers(data):
    if not data["flowers"]:
        print("Нет записей для отображения.")
        return
    for flower in data["flowers"]:
        display_flower(flower)

# Вывод цветка по ID
def display_flower_by_id(data):
    try:
        search_id = int(input('Введите ID записи которую хотите вывести: '))
    except ValueError:
        print("Ошибка ввода. Нужно ввести число.")
        return
    
    found = False
    for flower in data["flowers"]:
        if flower["id"] == search_id:
            display_flower(flower)
            found = True
            break
    if not found:
        print("Запись с таким ID не найдена.")

# Добавление нового цветка
def add_flower(data):
    print('Вы выбрали записать новую запись (новый цветок), вводите данные: ')
    
    try:
        new_id = int(input("Введите ID: "))
    except ValueError:
        print("Ошибка ввода. Нужно ввести число для ID.")
        return

    # Проверка уникальности ID
    for flower in data["flowers"]:
        if flower["id"] == new_id:
            print("Ошибка: цветок с таким ID уже существует!")
            return

    name = input("Введите название цветка: ")
    latin_name = input("Введите латинское название: ")
    
    is_red_book = input("Входит ли в Красную книгу? (true/false): ").strip().lower() == "true"
    
    try:
        price = float(input("Введите цену: "))
    except ValueError:
        print("Ошибка ввода. Нужно ввести число для цены.")
        return

    new_flower = {
        "id": new_id,
        "name": name,
        "latin_name": latin_name,
        "is_red_book_flower": is_red_book,
        "price": price
    }
    data["flowers"].append(new_flower)
    save_data(data)
    print("Запись прошла успешно")

# Удаление цветка по ID
def delete_flower_by_id(data):
    try:
        delete_id = int(input("Введите ID записи, которую хотите удалить: "))
    except ValueError:
        print("Ошибка ввода. Нужно ввести число.")
        return
    
    flowers = data["flowers"]
    found = False
    for i, flower in enumerate(flowers):
        if flower["id"] == delete_id:
            del flowers[i]
            found = True
            print(f"Запись с ID {delete_id} удалена.")
            break
    if not found:
        print(f"Запись с таким ID не найдена.")
    save_data(data)

# Главная функция
def main():
    print('start code')
    
    data = load_data()
    if data is None:
        return
    
    count_actions = 0
    
    while True:
        print('1 - Вывести все записи\n2 - Вывести запись по ID\n3 - Добавить запись\n4 - Удалить запись по ID\n5 - Выйти из программы')
        try:
            action = int(input("Выберите действие: "))
        except ValueError:
            print("Ошибка ввода. Нужно ввести число.")
            continue
        print()
        
        if action == 1:
            count_actions += 1
            display_all_flowers(data)
        elif action == 2:
            count_actions += 1
            display_flower_by_id(data)
        elif action == 3:
            count_actions += 1
            add_flower(data)
        elif action == 4:
            count_actions += 1
            delete_flower_by_id(data)
        elif action == 5:
            print(f'Вы провели {count_actions} операций с записями за время работы программы')
            print('Программа завершена')
            break
        else:
            print('Ошибка ввода. Попробуйте снова.')
    print('end code')

if __name__ == "__main__":
    main()