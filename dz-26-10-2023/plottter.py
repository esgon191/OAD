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

fig, ax = plt.subplots()

#plt setup
plt.title('S-кривая', loc='left')
plt.xlabel('Период')
plt.ylabel('% За период')
plt.style.use('ggplot')
plt.grid(axis='y')

#тики под осями
ax.set_xticks(range(len(data['План/Факт/Прогноз'])))
plt.xticks(rotation='vertical')
ax.set_xticklabels(data['План/Факт/Прогноз'])

x = list(range(len(data['План/Факт/Прогноз'])))

ax.bar(*oblast_opr(x, data['План за период']), color='#548ed5', label='План за период')
ax.bar(*oblast_opr(x, data['Факт за период']), color='#d99694', label='Факт за период')
ax.plot(*oblast_opr(x, data['План накопительно']), color='#416ea6', linestyle='-', label='План накопительно')
ax.plot(*oblast_opr(x, data['Факт накопительно']), color='#a8413f', linestyle='-', label='Факт накопительно')
ax.plot(*oblast_opr(x, data['Прогноз накопительно']), color='#00b050',linestyle='--', label='Прогноз накопительно')
plt.show()
