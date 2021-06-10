import csv


def data_import(filename):
    list1 = []
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        for i in file_reader:
            list1.append(list(i))
    # if len(list1):
        # print("Импорт данных из файла прошел успешно!")
    # else:
        # print("Произошла ошибка при импорте данных из файла!")
    return list1


def data_export(filename, list1):
    file = open(filename, 'w', encoding='utf-8')
    with file:
        writer = csv.writer(file)
        writer.writerows(list1)
    # print("Экспорт данных в файл прошел успешно!")


