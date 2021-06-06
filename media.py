class Media(object):
    def __init__(self):
        pass


class Link(Media):
    def __init__(self, protocol, host, way):
        self.protocol = protocol
        self.host = host
        self.way = way

# set methods

    def set_protocol(self, protocol):
        self.protocol = protocol

    def set_host(self, host):
        self.host = host

    def set_way(self, way):
        self.way = way

# get methods

    def get_protocol(self):
        return self.protocol

    def get_host(self):
        return self.host

    def get_way(self):
        return self.way


class Video(Media):
    def __init__(self, name, file):
        self.name = name
        self.file = file

# set methods

    def set_name(self, name):
        self.name = name

    def set_file(self, file):
        self.file = file

# get methods

    def get_name(self):
        return self.name

    def get_file(self):
        return self.file

# Моя Викусенька
print("Надо было терпеть до туалета. Но я же не терпила.(С) СТЕТХЭМ")