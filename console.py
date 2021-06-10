from book import Book as Bk
from porting import data_import
from porting import data_export


import_filename = "import.csv"
bk_list = []
export_filename = "export.csv"


def main():
    # Импорт данных
    for i in data_import(import_filename):
        bk1 = Bk()
        list1 = list(i)
        bk1.name.set(list1[0])
        bk1.author.set(list1[1])
        bk1.year.set(list1[2])
        bk1.publisher.set(list1[3])
        bk1.description.set(list1[4])
        bk_list.append(bk1)
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
                    bk1 = bk_list[i]
                    print(f"Имя: {bk1.name.get()}")
                    print(f"Автор: {bk1.author.get()}")
                    print(f"Год: {bk1.year.get()}")
                    print(f"Издатель: {bk1.publisher.get()}")
                    print(f"Описание: {bk1.description.get()}")
            else:
                print("\nПУСТО!")
        elif n == 2:
            print(f"\nНОВАЯ КНИГА:")
            bk1 = Bk()
            bk1.name.set(input("Имя: "))
            bk1.author.set(input("Автор: "))
            bk1.year.set(int(input("Год: ")))
            bk1.publisher.set(input("Издатель: "))
            bk1.description.set(input("Описание: "))
            bk_list.append(bk1)
            print(f"Новая книга успешно добавлена!")
        elif n == 3:
            i = int(input("\nИЗМЕНЕНИЕ КНИГИ №"))
            if i - 1 < len(bk_list):
                bk1 = Bk()
                bk1.name.set(input("Имя: "))
                bk1.author.set(input("Автор: "))
                bk1.year.set(int(input("Год: ")))
                bk1.publisher.set(input("Издатель: "))
                bk1.description.set(input("Описание: "))
                bk_list[i - 1] = bk1
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
    for bk1 in bk_list:
        list2 = list()
        list2.append(bk1.name.get())
        list2.append(bk1.author.get())
        list2.append(bk1.year.get())
        list2.append(bk1.publisher.get())
        list2.append(bk1.description.get())
        list1.append(list2)
    data_export(export_filename, list1)


main()

