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
        return int(input("Enter "))

    @staticmethod
    def list(data):
        print("List")
        pass

    @staticmethod
    def add(data):
        print("add")
        return data

    @staticmethod
    def change(data):
        print("Change")
        return data

    @staticmethod
    def delete(data):
        print("Delete")
        return data

    @staticmethod
    def exit():
        print("Exit")
        pass

    @staticmethod
    def error():
        print("Error")
        pass


class Console(Interface):
    pass


class Window(Interface):
    pass
