import csv


def csv_read(filename):
    list1 = list()
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        for i in file_reader:
            list1.append(list(i))
    return list1


def csv_write(filename, list1):
    s = str()
    for i in list1:
        s = s + ','.join(i) + '\n'
    with open(filename, 'w', encoding='utf-8') as file:
        for i in s:
            file.write(str(i))

