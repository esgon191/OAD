import csv
from progress.bar import *
data = dict()

def calculate(month_number, year_number, pid, type_op, table):
    res = 0
    for opid in table.keys():
        if type_op == table[opid]['type'] and pid == table[opid]['project_id']:
            if month_number != -1 and year_number != -1:
                if month_number == table[opid]['month'] and year_number == table[opid]['year']:
                    res += table[opid]['sum']

            else:
                res += table[opid]['sum']

    return res

with open('Справочник_должностей.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['dol'] = dict()
    for row in reader:
        data['dol'][int(row['id'])] = {
                'name': row['ФИО'],
                'dol': row['Должность']
                }


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
                'id' : int(row['id']),
                'name' : row['Наименование_проекта'],
                'phase' : row['Фаза_проекта'],
                'code' : row['Код_проекта'],
                'start' : row['Начало_фазы'],
                'end' : row['Конец_фазы'],
                'type' : int(row['Тип']),
                'place' : row['Местоположение'],
                'phase_budget' : int(row['Бюджет_текущей_фазы'].replace(' ', '')),
                'lprid' : int(row['ЛПР']),
                'managerid' : int(row['Менеджер_проекта']),
                'project_budget' : int(row['Бюджет_проекта'].replace(' ', ''))
            })



with open('История_расходов.csv', 'r', encoding='utf-8', newline='') as input_file:
    reader = csv.DictReader(input_file)
    data['history'] = dict()
    for row in reader:
        data['history'][int(row['Id_операции'])] = {
                'type' : 1 if row['Тип операции'] == 'Входящая' else -1,
                'project_id' : int(row['Id_проекта']),
                'year' : int(row['Год']),
                'month' : int(row['Номер_месяца']),
                'sum' : int(row['Сумма'][:-2].replace('\xa0', '').replace(' ', ''))
                }




with open('Витрина.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ('Наименование_проекта',
                  'Код_проекта',
                  'Фаза_проекта',
                  'Начало_фазы',
                  'Конец_фазы',
                  'Тип',
                  'Местоположение',
                  'Бюджет_текущей_фазы',
                  'ЛПР',
                  'Менеджер_проекта',
                  'Бюджет_проекта',
                  'Расход_август_2021',
                  'Расход_сентябрь_2021',
                  'Расход_октбярь_2021', 
                  'Расход_3_квартал_2021'
                  )
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for elem in data['cards']:
        rhs_8 = calculate(8, 2021, elem['id'], -1, data['history'])
        rhs_9 = calculate(9, 2021, elem['id'], -1, data['history'])
        rhs_10 = calculate(10, 2021, elem['id'], -1, data['history'])
        writer.writerow({
            'Наименование_проекта' : elem['name'],
            'Код_проекта' : elem['code'],
            'Фаза_проекта' : elem['phase'],
            'Начало_фазы' : elem['start'],
            'Конец_фазы' : elem['end'],
            'Тип' : elem['type'],
            'Местоположение' : elem['place'],
            'Бюджет_текущей_фазы' : elem['phase_budget'],
            'ЛПР' : data['dol'][elem['lprid']]['name'],
            'Менеджер_проекта' :  data['dol'][elem['managerid']]['name'],
            'Бюджет_проекта' : elem['project_budget'],
            'Расход_август_2021' : rhs_8,
            'Расход_сентябрь_2021' : rhs_9,
            'Расход_октбярь_2021' : rhs_10, 
            'Расход_3_квартал_2021' : rhs_8 + rhs_9 + rhs_10
            })


with open('Менеджеры.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ('Менеджер', 'Расход')
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    man = {i : 0 for i in list(set([j['managerid'] for j in data['cards']]))}
    
    for elem in data['cards']:
        man[elem['managerid']] += calculate(-1, -1, elem['id'], -1, data['history'])
    
    for elem in man.keys():
        writer.writerow({
            'Менеджер' : data['dol'][elem]['name'],
            'Расход' : man[elem] 
            })
