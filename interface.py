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
        return int(input("Введите цифру: "))

    @staticmethod
    def list(data):
        print("Список: ")
        pass

    @staticmethod
    def add(data):
        print("Добавление: ")
        return data

    @staticmethod
    def change(data):
        print("Изменение: ")
        return data

    @staticmethod
    def delete(data):
        print("Удаление: ")
        return data

    @staticmethod
    def exit():
        print("Выход! ")
        pass

    @staticmethod
    def error():
        print("Ошибка! ")
        pass


class Console(Interface):
    pass


class Window(Interface):
    pass
