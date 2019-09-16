"""
Задание 3 - CSV
 
Создайте список словарей:
    [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

Запишите содержимое списка словарей в файл в формате csv
"""

import csv
 

DATA = [ 
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]


def main():
    fields = [key for key, val in DATA[0].items()]
    with open('export.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(DATA)
#        for row in DATA:
#            writer.writerow(row)


if __name__ == '__main__':
    main()