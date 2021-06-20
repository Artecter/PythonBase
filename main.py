from convert import sql_request as sql
from convert import csv_read as read
from convert import csv_write as write
from convert import pdf_writer as pdf
from menu import main as menu

filename = "data.csv"

sql(filename)
data_list = read(filename)
print(data_list)
data_list = menu(data_list)
print(data_list)
write(filename, data_list)
pdf(filename)

