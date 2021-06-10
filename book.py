from attribute import Attribute as Att


class Book(object):
    def __init__(self, name="", author="", year=0, publisher="", description="", picture="", isbn=0):
        self.name = Att(name)
        self.author = Att(author)
        self.year = Att(int(year))
        self.publisher = Att(publisher)
        self.description = Att(description)
        self.picture = Att(picture)
        self.isbn = Att(isbn)

    def name(self):
        return self.name()

    def author(self):
        return self.author()

    def year(self):
        return self.year()

    def publisher(self):
        return self.publisher()

    def description(self):
        return self.description()

    def picture(self):
        return self.picture()

    def isbn(self):
        return self.isbn()
