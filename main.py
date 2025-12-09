import json

# Загрузка данных из файла
def load_data():
    with open('flowers.json', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Сохранение данных в файл
def save_data(data):
    with open('flowers.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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
def display_all_flowers(flowers):
    for flower in flowers:
        display_flower(flower)

# Вывод цветка по ID
def display_flower_by_id(flowers):
    search_id = int(input('Введите ID записи которую хотите вывести: '))
    found = False
    for flower in flowers:
        if flower["id"] == search_id:
            display_flower(flower)
            found = True
            break
    if not found:
        print("Запись с таким ID не найдена.")

# Добавление нового цветка
def add_flower(data):
    print('Вы выбрали записать новую запись (новый цветок), вводите данные: ')
    new_id = int(input("Введите ID: "))

    # Проверка уникальности ID
    for flower in data["flowers"]:
        if flower["id"] == new_id:
            print("Ошибка: цветок с таким ID уже существует!")
            return

    new_flower = {
        "id": new_id,
        "name": input("Введите название цветка: "),
        "latin_name": input("Введите латинское название: "),
        "is_red_book_flower": input("Входит ли в Красную книгу? (true/false): ").strip().lower() == "true",
        "price": float(input("Введите цену: "))
    }
    data["flowers"].append(new_flower)
    save_data(data)
    print("Запись прошла успешно")

# Удаление цветка по ID
def delete_flower_by_id(data):
    delete_id = int(input("Введите ID записи, которую хотите удалить: "))
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
    flowers = data['flowers']
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
            display_all_flowers(flowers)
        elif action == 2:
            count_actions += 1
            display_flower_by_id(flowers)
        elif action == 3:
            count_actions += 1
            add_flower(data)
            flowers = data['flowers']
        elif action == 4:
            count_actions += 1
            delete_flower_by_id(data)
            flowers = data['flowers']
        elif action == 5:
            print(f'Вы провели {count_actions} операций с записями за время работы программы')
            print('Программа завершена')
            break
        else:
            print('Ошибка ввода. Попробуйте снова.')
    print('end code')

main()
