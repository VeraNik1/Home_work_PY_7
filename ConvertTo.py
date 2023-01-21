
import function as fn
import csv
import json

file_names = fn.titles.keys()
#реализация конвертации в csv
def ConvertToCSV(file_names):
    for item in file_names:
        with open(item, 'r', encoding='UTF-8') as file,\
        open(item[:-3]+'csv', 'w+', encoding='UTF-8') as out:
            fieldnames = fn.titles[item]
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            writer.writeheader()
            for row in file:
                writer.writerow({k: v for k, v in zip(fieldnames, row.rstrip().split(','))})  

#реализация конвертации в json
def ConvertToJSON(file_names):
    for item in file_names:
        with open(item, 'r', encoding='UTF-8') as file:
            fieldnames = fn.titles[item]
            result= []
            for row in file:
                temp = {k: v for k, v in zip(fieldnames, row.rstrip().split(','))}
                result.append(temp)
        with open(item[:-3]+'json', 'w', encoding='UTF-8') as out:
            json.dump(result, out, indent=3, ensure_ascii=False) 

#меню конвертации
def letsConvertIt():
    print('''1 - Конвертировать в .csv",
2 - Конвертировать в .json"
3 - Отменить конвертацию''')
    while True:
        n = input()
        if n == '1': 
            ConvertToCSV(file_names)
            break
        elif n == '2': 
            ConvertToJSON(file_names)
            break
        elif n == '3': 
            break
        else: 
            print("Введено некорректное значение!")
    