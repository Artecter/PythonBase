from media import Book as Bk
from porting import data_import
from porting import data_export


import_filename = "data.csv"
bk_list = []
export_filename = "data.csv"


def main():
    # Импорт данных
    for i in data_import(import_filename):
        bk = Bk()
        list1 = list(i)
        bk.name.set(list1[0])
        bk.author.set(list1[1])
        bk.year.set(list1[2])
        bk.publisher.set(list1[3])
        bk.description.set(list1[4])
        bk_list.append(bk)
    # Обработка данных
    while True:
        print(f"\nВведите цифру от 1 до 5:")
        print(f"1 - список книг")
        print(f"2 - добавить книгу")
        print(f"3 - изменить книгу")
        print(f"4 - удалить книгу")
        print(f"5 - выход")
        n = int(input("Ваш выбор: "))
        if n == 1:
            print(f"\nСПИСОК КНИГ:")
            if len(bk_list):
                for i in range(len(bk_list)):
                    print(f"\nКНИГА №{i + 1}")
                    bk = bk_list[i]
                    print(f"Имя: {bk.name.get()}")
                    print(f"Автор: {bk.author.get()}")
                    print(f"Год: {bk.year.get()}")
                    print(f"Издатель: {bk.publisher.get()}")
                    print(f"Описание: {bk.description.get()}")
            else:
                print("\nПУСТО!")
        elif n == 2:
            print(f"\nНОВАЯ КНИГА:")
            bk = Bk()
            bk.name.set(input("Имя: "))
            bk.author.set(input("Автор: "))
            bk.year.set(int(input("Год: ")))
            bk.publisher.set(input("Издатель: "))
            bk.description.set(input("Описание: "))
            bk_list.append(bk)
            print(f"Новая книга успешно добавлена!")
        elif n == 3:
            i = int(input("\nИЗМЕНЕНИЕ КНИГИ №"))
            if i - 1 < len(bk_list):
                bk = Bk()
                bk.name.set(input("Имя: "))
                bk.author.set(input("Автор: "))
                bk.year.set(int(input("Год: ")))
                bk.publisher.set(input("Издатель: "))
                bk.description.set(input("Описание: "))
                bk_list[i - 1] = bk
                print(f"Книга №{i} успешно изменена!")
            else:
                print("Неверный номер книги!")
        elif n == 4:
            i = int(input("\nУДАЛЕНИЕ КНИГИ №"))
            if i - 1 < len(bk_list):
                del bk_list[i - 1]
                print(f"Книга №{i} успешно удалена!")
            else:
                print("Неверный номер книги!")
        elif n == 5:
            break
        else:
            print("\nНеверная цифра, попробуйте еще раз!")
    print(f"\nВЫХОД!")
    # Экспорт данных
    list1 = list()
    for bk in bk_list:
        list2 = list()
        list2.append(bk.name.get())
        list2.append(bk.author.get())
        list2.append(bk.year.get())
        list2.append(bk.publisher.get())
        list2.append(bk.description.get())
        list1.append(list2)
    data_export(export_filename, list1)

