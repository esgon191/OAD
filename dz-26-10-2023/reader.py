import csv
def read():
    data = {}
    with open('Данные для S-кривой.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        #чтение построчно, пустые поля заполняем нулями для удобства
        for line in csvreader:
            data[line[0]] = ['-1.0%' if i == '' else i for i in line[1:]]

        for key in list(data.keys())[1:]:
            data[key] = [float(i.replace(',', '.')[:-1]) for i in data[key]]

    return data

#print(read())
