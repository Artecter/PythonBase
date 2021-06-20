from interface import Interface


def main(data: object) -> object:
    menu = Interface()
    while True:
        choice = menu.choice()
        if choice == 1:
            menu.list(data)
        elif choice == 2:
            data = menu.add(data)
        elif choice == 3:
            data = menu.change(data)
        elif choice == 4:
            data = menu.delete(data)
        elif choice == 5:
            menu.exit()
            break
        else:
            menu.error()
            continue
    return data
