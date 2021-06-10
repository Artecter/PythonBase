from attribute import Attribute as Att


class Media(object):
    def __init__(self):
        pass


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


class Video(Media):
    def __init__(self, name, file):
        self.name = Att(name)
        self.file = Att(file)

    def name(self):
        return self.name

    def file(self):
        return self.file
