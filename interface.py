def enum(data):
    text = "Список: "
    raw = 1
    for i in data[1:]:
        col = 1
        text = text + f"\n\n{data[0][0]} №{raw}"
        for j in i[1:]:
            text = text + f"\n{data[0][col]}: {j}"
            col = col + 1
        raw = raw + 1
    return text


def add(data, new_info):
    list1 = list(str(int(data[-1][0])+1))
    for i in new_info:
        list1.append(i)
    data.append(list1)
    return data


def change(data, number, new_info):
    if int(number) > int(data[-1][0]):
        return data
    list1 = list(str(number))
    for i in new_info:
        list1.append(i)
    data[int(number)][:] = list1
    return data


def delete(data, number):
    if int(number) > int(data[-1][0]):
        return data
    data.remove(data[:][int(number)])
    return data


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class Interface(Singleton):
    def __init__(self, data):
        self.data = data

    def choice(self):
        return 0

    def enum(self):
        return enum(self.data)

    def add(self, new_info):
        return add(self.data, new_info)

    def change(self, number, new_info):
        return change(self.data, number, new_info)

    def delete(self, number):
        return delete(self.data, number)

    def exit(self):
        pass

    def error(self):
        pass

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class Console(Interface):
    def choice(self):
        return int(input(f"\n1 - список\n2 - добавить\n3 - изменить\n4 - удалить\n5 - выйти\nВыбор: "))

    def enum(self):
        print(enum(self.data))

    def add(self, new_info=[]):
        print(f"Добавление: ")
        new_info = list()
        for i in self.data[0][1:]:
            new_info.append(input(f"{i}: "))
        return add(self.data, new_info)

    def change(self, number=0, new_info=[]):
        print(f"Изменение: ")
        new_info = list()
        number = input(f"{self.data[0][0]} №")
        for i in self.data[0][1:]:
            new_info.append(input(f"{i}: "))
        return change(self.data, number, new_info)

    def delete(self, number=0):
        print(f"Удаление: ")
        number = input(f"{self.data[0][0]} №")
        return delete(self.data, number)

    def exit(self):
        print("Выход! ")

    def error(self):
        print("Ошибка! ")


class Window(Interface):
    pass
