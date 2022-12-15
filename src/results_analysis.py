## load packages from (same to load functions)
import sys
from numpy import shape
import csv
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

## result analysis on the output of wind cases

with open('results/Dec11_sample_1_wind_hourly_daily_average_label.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
# store data by rows

print(shape(rows))
#print(rows[1][0])
#print(rows[1][0] == '')

data = [[]]*32

j=0
for i in range(shape(rows)[0]):
    if i % 2 == 1:
        pass
    else:
        data[j] = rows[i]
        j = j + 1

data = np.array(data, dtype=float)

print(shape(data)[1])
x = np.array([*range(shape(data)[1])])
#print(x)



plt.plot(x, data[0])
plt.xlim([0, 24])
plt.ylim([0, 1])
plt.show()

'''
## hourly results
with open('datasets/Solar_sub.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

rows = np.array(rows, dtype=float)
trX = []
print(shape(rows))
for x in range(rows.shape[1]):
    train = rows[:162480, x].reshape(-1, 24)
    # train = train / 16

    # print(shape(train))
    if trX == []:
        trX = train
    else:
        trX = np.concatenate((trX, train), axis=0)

print(shape(trX))
x = np.array([*range(shape(trX)[1])])
'''