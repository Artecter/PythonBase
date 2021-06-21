# 20.06.2021 Copyright Artecter

from convert import csv_read as read
from convert import csv_write as write
from convert import pdf_write as pdf
from window import application as window
from console import main as console

interface = open('config').read().split('\n')[0].split('=')[1]
filename = open('config').read().split('\n')[1].split('=')[1]
data = read(filename)

if interface:
    window(filename, data)
else:
    write(filename, console(data))

pdf(filename)





