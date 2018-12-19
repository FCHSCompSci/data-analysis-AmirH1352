#import matplotlib
import matplotlib.pyplot as plt
#import numpy as np
import statistics
import csv


atk = []
SP = []

filename = 'pokemon_alopez247.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        atk.append(int(row[6]))
    for row in reader:
        SP.append(int(row[8]))

minatk = []
minatk.append(min(atk))
#print(minatk)
maxatk = []
maxatk.append(max(atk))
#print(maxatk)
averageatk = []
averageatk.append(round(statistics.mean(atk)))
#print(averageatk)
minsp = []
minsp.append(min(SP))
#print(minsp)
maxsp = []
maxsp.append(max(SP))
#print(maxsp)
averagesp = []
averagesp.append(round(statistics.mean(SP)))

fig = plt.figure(dpi=128, figsize=(20, 15))
plt.plot(maxatk, c='red')
plt.plot(maxsp, c='blue')
plt.plot(minatk, c='yellow')
plt.plot(minsp, c='orange')
plt.plot(averageatk, c='purple')
plt.plot(averagesp, c='pink')

plt.title("comparing atk and special atk", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("stats", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

