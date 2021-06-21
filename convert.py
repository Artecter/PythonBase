# 20.06.2021 Copyright Artecter

import csv
import pandas as pd
import pdfkit as pdf


def csv_read(filename):
    list1 = list()
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        for i in file_reader:
            list1.append(list(i))
    return list1


def csv_write(filename, list1):
    s = str()
    for i in list1:
        s = s + ','.join(i) + '\n'
    with open(filename, 'w', encoding='utf-8') as file:
        for i in s:
            file.write(str(i))


# 21.06.2021 Copyright Eyonde

def pdf_write(csv_file):
    html_file = csv_file[:-3]+'html'
    pdf_file = csv_file[:-3]+'pdf'
    df = pd.read_csv(csv_file, sep=',')
    df.to_html(html_file)
    pdf.from_file(html_file, pdf_file)

