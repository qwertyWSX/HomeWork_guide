source_file = "guide.txt"
copy_file = "copy_guid.txt"


def add_tel():
    data = (
        input("Введите фамилию: "),
        input("Введите имя: "),
        input("Введите Отчество: "),
        input("Введите номер телефона: "),
    )
    write_data(source_file, data)
    print("Запись успешно добавлена")
    pass


def show_guide():
    data = get_guide()
    print_guide(data)
    pass


def copy_tel():
    data = get_guide()
    print_guide(data)
    try:
        num = int(input("Введите номер записи: "))
    except:
        print("Ошибка! Введите целое число.")
        return -1
    if num not in range(1, len(data)):
        print("Ошибка! Такой записи нет.")
        return -1
    else:
        write_data(copy_file, data[num - 1])
        return 1


def find_tel():
    st = input("Введите строку для поиска: ")
    data = get_guide()
    new_data = []
    for row in data:
        for el in row:
            if st.lower() in el.lower():
                new_data.append(row)
                break
    if len(new_data) < 1:
        print("Запись не найдена")
    else:
        print_guide(new_data)


def get_guide():
    data = []
    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            l = line.split()
            data.append(l)
    return data


def print_guide(data: list):
    print("-" * 45)
    for row in enumerate(data, 1):
        print(row[0], end=". ")
        for el in row[1]:
            print(el, end=" ")
        print()
    print("-" * 45)


def write_data(file, data):
    with open(file, "a", encoding="utf-8") as f:
        st = " ".join(data)
        f.write(st + "\n")


def menu():
    dct = {
        "cr": (add_tel, "Добавить запись"),
        "sh": (show_guide, "Вывести справочник"),
        "cp": (copy_tel, "Скопировать запись в новый справочник"),
        "fn": (find_tel, "Поиск записи в файле"),
        "ex": (exit, "Выйти из программы"),
    }

    for key, val in dct.items():
        print(key, val[1], sep=" - ")

    cmd = input("Введите команду: ")
    if cmd not in dct.keys():
        return -1
    else:
        return dct[cmd][0]


while True:
    cmd = menu()
    if cmd != -1:
        cmd()
        input("Для продолжения нажмите enter...")
        print()
    else:
        input("Такой команды нет, для продолжения введите enter...")
        print()
