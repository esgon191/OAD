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

#считание данных из подготовленной csvшки
data = reader.read()

#создание координат по Оx
x = np.arange(0, len(data['План/Факт/Прогноз']), 1)

plt.rcParams['figure.figsize'] = [16, 9]

#создание окна и левой оси y
fig, ax_left = plt.subplots()

plt.title('S-кривая по проекту "обустройство месторождения"',  
    fontdict={"fontsize": 16, 
                "fontweight": "bold"})

#подпись под осью x
ax_left.set_xticks(range(len(data['План/Факт/Прогноз'])))
plt.xticks(rotation='vertical')
ax_left.set_xticklabels(data['План/Факт/Прогноз'], fontsize=8)

#ax_left
ax_left.set_ylabel('% за период') 
ax_left.bar(*oblast_opr(x, data['План за период']), color='#548ed5', label='План за период')
ax_left.bar(*oblast_opr(x, data['Факт за период']), color='#d99694', label='Факт за период')
ax_left.tick_params(axis ='y') 
ax_left.set_ylim(0, 20)
ax_left.grid(axis='y')

#ax_right
ax_right = ax_left.twinx()
ax_right.set_ylabel('% накопительно')
ax_right.plot(*oblast_opr(x, data['План накопительно']), color='#416ea6', linestyle='-', label='План накопительно')
ax_right.plot(*oblast_opr(x, data['Факт накопительно']), color='#a8413f', linestyle='-', label='Факт накопительно')
ax_right.plot(*oblast_opr(x, data['Прогноз накопительно']), color='#00b050',linestyle='--', label='Прогноз накопительно')
ax_right.set_ylim(0, 100)
ax_right.tick_params(axis ='y') 

#legend
fig.add_artist(ax_left.legend(loc='upper right'))
fig.add_artist(ax_right.legend(loc='center right'))
#fig.legend(loc='center right')

plt.show()
