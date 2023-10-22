import matplotlib.pyplot as plt
import numpy as np
import reader

def oblast_opr(x, y):
    #возвращает такой массив x, где для каждого xi существует yi из массива y
    #изначально x = list(range(len(y)));
    #"несуществующие" yi равны -1.0
    xnew, ynew = [], []
    for i in range(len(y)):
        if y[i] != -1:
            ynew.append(y[i])
            xnew.append(x[i])

    return xnew, ynew


data = reader.read()

plt.style.use('ggplot')

fig, ax = plt.subplots()

x = list(range(len(data['План/Факт/Прогноз'])))

for data_param in list(data.keys())[1:]:
    ax.plot(*oblast_opr(x, data[data_param]))
    #ax.plot(x, data[data_param])   

plt.show()
