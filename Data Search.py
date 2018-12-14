import matplotlib as plt
import numpy as np
import statistics
import csv


filename = 'pokemon_alopez247.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    high_atk = [ ]
    for row in reader:
        atk = int(row[6])
        high_atk.append(atk)
    #print(high_atk)
    high_spatk = []
    for row in reader:
        SP = int(row[8])
        high_spatk.append(SP)
    #print(high_spatk)

minatk = []
minatk.append(min(high_atk))
#print(minatk)
maxatk = []
maxatk.append(max(high_atk))
#print(maxatk)
averageatk = []
averageatk.append(round(statistics.mean(high_atk)))
#print(averageatk)
minsp = []
minsp.append(min(high_spatk))
maxsp = []
maxsp.append(max(high_spatk))
averagesp = []
averagesp.append(round(statistics.mean(high_spatk)))

N = 3
ind = np.arange(N)
width = 0.45

p1 = plt.bar(ind, minatk, width, yerr=maxatk)
p2 = plt.bar(ind, minsp, width, bottom=minatk, yerr=maxsp)
p3 = plt.bar(ind, averageatk, width, bottom=averagesp)

plt.ylabel('atk / sp_atk Power')
plt.title('The minimal, maximum, and average atk/sp_atk of all pokemon')
plt.xticks(ind, ('Max', 'Min', 'Average'))
plt.yticks(np.arange(0, 80, 5))
plt.legend((p1[0], p2[0], p3[0]), ('Atk', 'SP_Atk'))

plt.show()

