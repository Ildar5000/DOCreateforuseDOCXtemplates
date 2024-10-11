import os
import csv
import time
import docx
from docxtpl import DocxTemplate

# словарь
keyWords = {}


# погружаем словарь
def LoadCSV():
    with open('KeyWords.txt', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            context = {row[0]: row[1]}
            keyWords.update(context)


LoadCSV();

# Указываем путь к директории
dirname = os.path.dirname(__file__)
directory = dirname+'/template'

# Получаем список файлов
files = os.listdir(directory)

# проходим по файлам
for item in files:
    doc = DocxTemplate(directory+'/'+item)
    doc.render(keyWords)
    doc.save("ready/"+"final"+item)
# context = { 'director' : "И.И.Иванов"}
# doc.render(context)
# doc.save("шаблон-final.docx")
