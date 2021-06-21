from convert import csv_read as read
from convert import csv_write as write
from convert import pdf_write as pdf
from interface import Console_menu as Menu

filename = "videos.csv"

menu = Menu(read(filename))
while True:
    choice = menu.choice()
    if choice == 1:
        menu.enum()
    elif choice == 2:
        menu.add()
    elif choice == 3:
        menu.change()
    elif choice == 4:
        menu.delete()
    elif choice == 5:
        menu.exit()
        break
    else:
        menu.error()
        continue
write(filename, menu.get_data())

# pdf(filename)





