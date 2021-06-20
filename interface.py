class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class Interface(Singleton):
    def __init__(self):
        pass

    def write(self, text):
        pass
