class Book(object):
    def __init__(self, name="", author="", year=0, publisher="", description="", picture="", isbn=0):
        self.name = name
        self.author = author
        self.year = int(year)
        self.publisher = publisher
        self.description = description
        self.picture = picture
        self.isbn = isbn

# set methods

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_description(self, description):
        self.description = description

    def set_picture(self, picture):
        self.picture = picture

    def set_isbn(self, isbn):
        self.isbn = isbn

# get methods

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_description(self):
        return self.description

    def get_picture(self):
        return self.picture

    def get_isbn(self):
        return self.isbn
