from interface import Interface


def error():
    # Interface.error()
    print("Error")


def exit():
    # Interface.exit()
    print("Exit")


def data_delete(data):
    # data = Interface.delete(data)
    print("Delete")
    return data


def data_change(data):
    # data = Interface.change(data)
    print("Change")
    return data


def data_add(data):
    # data = Interface.add(data)
    print("Add")
    return data


def data_list(data):
    # data = Interface.list(data)
    print("List")
    pass


def choice():
    # digit = Interface.choice()
    digit = int(input("Enter "))
    return digit


def main(data):
    while True:
        answer = choice()
        if answer == 1:
            data_list(data)
        elif answer == 2:
            data = data_add(data)
        elif answer == 3:
            data = data_change(data)
        elif answer == 4:
            data = data_delete(data)
        elif answer == 5:
            exit()
            break
        else:
            error()
            continue
    return data
