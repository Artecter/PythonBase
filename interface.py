class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class Interface(Singleton):
    def __init__(self):
        pass

    @staticmethod
    def choice():
        return int(input(f"\n1 - список\n2 - добавить\n3 - изменить\n4 - удалить\n5 - выход\nВведите цифру: "))

    @staticmethod
    def list(data):
        print(f"\nСписок: ")
        for i in data[1:]:
            count = 1
            print(f"\n{data[0][0]} №{i[0]}")
            for j in i[1:]:
                print(data[0][count], end=": ")
                print(j)
                count = count + 1
        pass

    @staticmethod
    def add(data):
        print(f"\nДобавление: ")
        new = list()
        new.append(str(int(data[-1][0])+1))
        for i in data[0][1:]:
            new.append(str(input(f"{i}: ")))
        data.append(new)
        return data

    @staticmethod
    def change(data):
        print(f"\nИзменение: ")
        return data

    @staticmethod
    def delete(data):
        print(f"\nУдаление: ")
        return data

    @staticmethod
    def exit():
        print(f"\nВыход! ")

    @staticmethod
    def error():
        print(f"\nОшибка! ")


class Console(Interface):
    pass


class Window(Interface):
    pass
