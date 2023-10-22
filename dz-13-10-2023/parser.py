import csv

#Формулы расчета прибавки к рейтингу. Очевидно некорректны.
#Инструкция для формирования корректного рейтинга есть на портале "mos.ru".
#Однако для формирования такого рейтинга требуемые данные выходят за рамки ТЗ
#и вообще не представлены на портале открытых данных.

def calc_ege(mega_data, data_ege):
	for line in data_ege:
		mega_data[line['global_id']] += line['PASSES_OVER_220'] / (0.03 if line['PASSER_UNDER_160'] == 0 else line['PASSER_UNDER_160'])

	return mega_data

def calc_oge(mega_data, data_oge):
	for line in data_oge:
		mega_data[line['global_id']] += line['OGE_SCORE']

	return mega_data

def calc_olymp(mega_data, data_olymp):
	for line in data_olymp:
		mega_data[line['global_id']] += (line['Class'] ** line['Stage']* line['Status'])/100

	return mega_data

def finder(global_id , data_list):
	for line in data_list:
		if line['global_id'] == global_id:
			return line['EDU_NAME']

	return False

def display(mega_data, data_olymp, data_ege, data_oge):
	for line in mega_data:
		name = finder(line[0], data_olymp)
		if name:
			print(name, line[1])
			continue

		name = finder(line[0], data_ege)
		if name:
			print(name, line[1])
			continue

		name = finder(line[0], data_oge)
		if name:
			print(name, line[1])
			




#Перенос всех нужных данных из фаЙлов в массивы 
#Представление по словарю в таком же формате, как в .csv 

data_ege = []

with open('data_ege.csv', 'r', encoding='utf-8', newline='') as input_file:
	reader = csv.DictReader(input_file)
	for row in reader:
		data_ege.append({
			'global_id' : int(row['global_id']),
		 	'YEAR' : row['YEAR'],
		 	'PASSES_OVER_220' : int(row['PASSES_OVER_220']),
		 	'PASSER_UNDER_160' : int(row['PASSER_UNDER_160']),
		 	'EDU_NAME' : row['EDU_NAME']
		 	})

data_oge = []

with open('data_oge.csv', 'r', encoding='utf-8', newline='') as input_file:
	reader = csv.DictReader(input_file)
	for row in reader:
		data_oge.append({
			'global_id' : int(row['global_id']), 
			'YEAR' : row['YEAR'], 
			'OGE_SCORE' : int(row['OGE_SCORE']),
			'EDU_NAME' : row['EDU_NAME']
			})

data_olymp = []

with open('data_olymp.csv', 'r', encoding='utf-8', newline='') as input_file:
	reader = csv.DictReader(input_file)
	for row in reader:
		data_olymp.append({
			'Status' : 1 if row['Status'] == 'призёр' else 3,
			'global_id' : int(row['global_id']), 
			'YEAR' : row['YEAR'], 
			'OlympiadType' : row['OlympiadType'], 
			'Stage' : int(row['Stage']) if len(row['Stage']) > 0 else 0, 
			'Class' : int(row['Class']),
			'EDU_NAME' : row['FullName']
			})

#генерация множества всех школ; такая операция нужна на случай если в каких-то 
#массивах выше отсутсвует информация по какой-то статье 
all_ids = set(sorted(list(set(
	[i['global_id'] for i in data_ege] + 
	[i['global_id'] for i in data_oge] 
	#+ [i['global_id'] for i in data_olymp]
))))
#генерация собственно рейтинга в виде словаря id : rating
mega_data = {i : 0 for i in all_ids}

#Собственно формирование рейтинга
mega_data = calc_ege(mega_data, data_ege)
mega_data = calc_oge(mega_data, data_oge)
#mega_data = calc_olymp(mega_data, data_olymp)
#Сортировка рейтинга по значениям
mega_data = sorted(mega_data.items(), key=lambda item: item[1])
print(len(mega_data), len(all_ids))
display(mega_data, data_olymp, data_ege, data_oge)
print(len(data_olymp), len(data_ege), len(data_oge))
#print(mega_data)