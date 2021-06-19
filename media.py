# Базовый класс Атрибут
class Attribute(object):
    def __init__(self, value):
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value


Att = Attribute


# Класс Медиа
class Media(object):
    def __init__(self):
        pass


# Класс Ссылка
class Link(Media):
    def __init__(self, protocol, host, way):
        self.protocol = Att(protocol)
        self.host = Att(host)
        self.way = Att(way)

    def protocol(self):
        return self.protocol

    def host(self):
        return self.host

    def way(self):
        return self.way


# Класс Видео
class Video(Media):
    def __init__(self, name, file):
        self.name = Att(name)
        self.file = Att(file)

    def name(self):
        return self.name

    def file(self):
        return self.file


# Класс Книга
class Book(Media):
    def __init__(self, name="", author="", year=0, publisher="", description="", picture="", isbn=0):
        self.name = Att(name)
        self.author = Att(author)
        self.year = Att(int(year))
        self.publisher = Att(publisher)
        self.description = Att(description)
        self.picture = Att(picture)
        self.isbn = Att(isbn)

    def name(self):
        return self.name

    def author(self):
        return self.author

    def year(self):
        return self.year

    def publisher(self):
        return self.publisher

    def description(self):
        return self.description

    def picture(self):
        return self.picture

    def isbn(self):
        return self.isbn
