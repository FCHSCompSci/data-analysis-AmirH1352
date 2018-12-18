import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import statistics
import csv
import collections as counter



filename = 'pokemon_alopez247.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    atk = []
    for row in reader:
        atk.append(int(row[6]))
    #print(high_atk)
    SP = []
    for row in reader:
        SP.append(int(row[8]))
    #print(high_spatk)

minatk = []
minatk.append(min(atk))
#print(minatk)
maxatk = []
maxatk.append(min(atk))
#print(maxatk)
#averageatk = []
#averageatk.append(round(statistics.mean(atk)))
#print(averageatk)
minsp = []
minsp.append(min(SP))
maxsp = []
maxsp.append(min(SP))

#averagesp = []
#averagesp.append(round(statistics.mean(SP)))

ind = np.arange(len(atk))
width = 0.45

fig, ax = plt.subplots( )
rects1 = ax.bar(ind - width/2, maxatk, width, yerr=minatk,
                color='red', label='atk')
rects2 = ax.bar(ind - width/2, maxsp, width, yerr=minsp, color='yellow')
#rects3 = ax.bar(ind - width/2, averageatk, width, yerr=averagesp,
                #color='blue')

ax.set_ylabel('power level')
ax.set_title('Pokemon atk and spatk')
ax.set_xticks(ind)
ax.set_xticklabels(('max', 'min'))
ax.legend()

def autolabel(rects, xpos='center'):
    xpos = xpos.lower()
    ha = {'center': 'center', 'right':'left', 'left':'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}
    for rect in rects:
        height = rect.getheight()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height, '{}'.format(height), ha=ha[xpos], va='bottom')

autolabel(rects1, 'left')
autolabel(rects2, 'right')
#autolabel(rects3, 'left')

plt.show()