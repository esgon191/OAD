import csv
from datetime import datetime

data = dict()

with open('Справочник_должностей.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['dol'] = []
    for row in reader:
        data['dol'].append({
            int(row['id']) : {
                'name': row['ФИО'],
                'dol': row['Должность']
                }
            })


with open('Справочник_типов.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['types'] = []
    for row in reader:
        data['types'].append({
                int(row['Id']) : row['Тип']
            })


with open('Карточки.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['cards'] = []
    for row in reader:
        data['cards'].append({
            int(row['id']) : {
                'name' : row['Наименование_проекта'],
                'code' : row['Код_проекта'],
                'start' : datetime.strptime(row['Начало_фазы'], '%d.%m.%y').date(),
                'end' : datetime.strptime(row['Конец_фазы'], '%d.%m.%y').date(),
                'type' : int(row['Тип']),
                'place' : row['Местоположение'],
                'phase_budget' : int(row['Бюджет_текущей_фазы']),
                'lprid' : int(row['ЛПР']),
                'managerid' : int(row['Менеджер_проекта']),
                'project_budget' : int(row['Бюджет_проекта'])
                }
            })



with open('История_расходов.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['history'] = []
    for row in reader:
        data['history'].append({
                int(row['id_операции']) : {
                        'type' : 1 if row['Тип операции'] == 'Входящая' else -1,
                        'project_id' : int(row['id_проекта']),
                        'date' : datetime.strptime(f'1.{row["Номер месяца"]}.{row["Год"]}', '%d.%m.%y').date(),
                        'sum' : int(row['Сумма'][:-1].replace(' ', ''))
                    }
            })


print(data)
