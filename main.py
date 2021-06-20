from convert import csv_read as read
from convert import csv_write as write
from menu import main as menu

filename = "data.csv"

print(read(filename))

write(filename, menu(read(filename)))

print(read(filename))

