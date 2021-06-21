# 20.06.2021 Copyright Artecter
from convert import csv_read as read
from convert import csv_write as write
from convert import pdf_write as pdf
from window import application as window
from console import main as console

interface = True
# 0 - Console, 1 - Window
filename = "videos.csv"
data = read(filename)

if interface:
    data = window(data)
else:
    data = console(data)

write(filename, data)

# pdf(filename)





