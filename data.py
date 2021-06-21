# 20.06.2021 Copyright Artecter

from singleton import Singleton


class Data(Singleton):
    def __init__(self, data_list):
        self.data_list = data_list

    def enum(self):
        text = "Список: "
        raw = 1
        for i in self.data_list[1:]:
            col = 1
            text = text + f"\n\n{self.data_list[0][0]} №{raw}"
            for j in i[1:]:
                text = text + f"\n{self.data_list[0][col]}: {j}"
                col = col + 1
            raw = raw + 1
        return text

    def add(self, new_info):
        list1 = list(str(int(self.data_list[-1][0]) + 1))
        for i in new_info:
            list1.append(i)
        self.data_list.append(list1)
        return self.data_list

    def change(self, number, new_info):
        if int(number) > int(self.data_list[-1][0]):
            return self.data
        list1 = list(str(number))
        for i in new_info:
            list1.append(i)
        self.data_list[int(number)][:] = list1
        return self.data_list

    def delete(self, number):
        if int(number) > int(self.data_list[-1][0]):
            return self.data_list
        self.data_list.remove(self.data_list[:][int(number)])
        return self.data_list
