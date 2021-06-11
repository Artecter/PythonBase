import csv


def data_import(filename):
    list1 = list()
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        for i in file_reader:
            list1.append(list(i))
    return list1


def data_export(filename, list1):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in list1:
            file.write(str(i))


def request(filename):
    pass




