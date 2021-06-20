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
        raw = 1
        for i in data[1:]:
            col = 1
            print(f"\n{data[0][0]} №{raw}")
            for j in i[1:]:
                print(data[0][col], end=": ")
                print(j)
                col = col + 1
            raw = raw + 1

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
        number = int(input(f"\n{data[0][0]} №"))
        new = list(str(number))
        for i in data[0][1:]:
            new.append(str(input(f"{i}: ")))
        data[number][:] = new
        return data

    @staticmethod
    def delete(data):
        print(f"\nУдаление: ")
        number = int(input(f"\n{data[0][0]} №"))
        data.remove(data[:][number])
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
