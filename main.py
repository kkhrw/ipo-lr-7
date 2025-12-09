# Короленко Ульяна
# Вариант 2
import json
# Запись файла json в data
def load_data():
    with open('flowers.json', encoding='utf-8') as file:
        data = json.load(file)
    return data
# Сохранение в json файл 
def save_data(data):
    with open('flowers.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Функция выводит все записи
def display_all_flowers(flowers):
    for flower in flowers:
        display_flower(flower)

# Функция выводит выводит информацию об одном цветке
def display_flower(flower):
    if flower["is_red_book_flower"] == False:
        print(f"============ {flower['name']} ============")
        print(f'Номер цветка - {flower["id"]}, Латинское название - {flower["latin_name"]}')
        print(f'{flower["name"]} не является краснокнижным цветком')
        print(f'=============== Цена: {flower["price"]} ===============')
        print()
    elif flower["is_red_book_flower"] == True:
        print(f"============ {flower['name']} ============")
        print(f'Номер цветка - {flower["id"]}, Латинское название - {flower["latin_name"]}')
        print(f'{flower["name"]} является краснокнижным цветком')
        print(f'=============== Цена: {flower["price"]} ===============')
        print()

# Функция выводит цветок по ID
def display_flower_by_id(flowers):
    num = int(input('Введите ID записи которую хотите вывести: ')) - 1
    print()
    found = False
    if num >= 0 and num < len(flowers):
        display_flower(flowers[num])
        found = True
    if not found:
        print("Запись с таким ID не найдена.")

# Функция добавляет цветок
def add_flower(data):
    print('Вы выбрали записать новую запись (новый цветок), вводите данные: ')
    new_flower = {
        "id": int(input("Введите ID: ")),
        "name": input("Введите название цветка: "),
        "latin_name": input("Введите латинское название: "),
        "is_red_book_flower": input("Входит ли в Красную книгу? (true/false): ").strip().lower() == "true",
        "price": input("Введите цену: ")
    }
    data["flowers"].append(new_flower)
    save_data(data)
    print("Запись прошла успешно")

# Функция удаляет цветок по ID
def delete_flower_by_id(data):
    delete_id = int(input("Введите ID записи, которую хотите удалить: "))
    flowers = data["flowers"]
    found = False
    for i in range(len(flowers)):
        if flowers[i]["id"] == delete_id:
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
    flowers = data['flowers']
    count_actions = 0
    
    while True:
        print(f'1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы')
        action = int(input("Выберите действие: "))
        print()
        
        if action == 1:
            count_actions += 1
            display_all_flowers(flowers)
        elif action == 2:
            count_actions += 1
            display_flower_by_id(flowers)
        elif action == 3:
            count_actions += 1
            add_flower(data)
            data = load_data()
            flowers = data['flowers']
        elif action == 4:
            count_actions += 1
            delete_flower_by_id(data)
            data = load_data()
            flowers = data['flowers']
        elif action == 5:
            print(f'Вы провели {count_actions} операций с записями за время работы программы')
            print('Программа завершена')
            break
        else:
            print('Ошибка ввода, ты идиот')
            break
    print('end code')
main()