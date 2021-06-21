# 20.06.2021 Copyright Artecter

from data import Data


class Console(object):
    def __init__(self, data):
        self.data = data

    def choice(self):
        return int(input(f"\n1 - список\n2 - добавить\n3 - изменить\n4 - удалить\n5 - выйти\nВыбор: "))

    def enum(self):
        print(Data(self.data).enum())

    def add(self,):
        print(f"Добавление: ")
        new_info = list()
        for i in self.data[0][1:]:
            new_info.append(input(f"{i}: "))
        return Data(self.data).add(new_info)

    def change(self):
        print(f"Изменение: ")
        new_info = list()
        number = input(f"{self.data[0][0]} №")
        for i in self.data[0][1:]:
            new_info.append(input(f"{i}: "))
        return Data(self.data).change(number, new_info)

    def delete(self):
        print(f"Удаление: ")
        number = input(f"{self.data[0][0]} №")
        return Data(self.data).delete(number)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def exit(self):
        print("Выход! ")

    def error(self):
        print("Ошибка! ")


def main(data):
    menu = Console(data)
    while True:
        choice = menu.choice()
        if choice == 1:
            menu.enum()
        elif choice == 2:
            menu.add()
        elif choice == 3:
            menu.change()
        elif choice == 4:
            menu.delete()
        elif choice == 5:
            menu.exit()
            break
        else:
            menu.error()
            continue
    return menu.get_data()

