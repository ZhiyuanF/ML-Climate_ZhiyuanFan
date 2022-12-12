## load packages from (same to load functions)
import sys
from numpy import shape
import csv
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

## process the data labels for daily average

with open('datasets/Wind_sub.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
# store data by rows
rows = np.array(rows, dtype=float)
# empty set of trX for storing the data
trX = []
print(shape(rows))

for x in range(rows.shape[1]):
    # truncate the data so it fits into x*576 dimension
    # reshape the data for 576 (24*24)
    train = rows[:-20, x].reshape(-1, 24)
    # print(shape(train))

    # add each training sample to the trX
    if trX == []:
        trX = train
    else:
        trX = np.concatenate((trX, train), axis=0)

print(shape(trX))

# make the mean for each training set to be its label
label_a = np.rint(np.mean(trX, axis = 1))

print(shape(label_a))

# combine the set of labels without enough entries
for i in range(label_a.shape[0]):
    if label_a[i] < 2.0:
        label_a[i] = 2.0
    elif label_a[i] > 15.0:
        label_a[i] = 15.0


print("Maximum value of average",max(label_a))
print("Minimum value of average",min(label_a))
print("Shape of the generated label", shape(label_a))

# count each label's occurance
unique, counts = np.unique(label_a, return_counts=True)
print(dict(zip(unique, counts)))

plt.hist(label_a, bins=int(max(label_a)-min(label_a)), density=True)
#plt.show()

pd.DataFrame(label_a).to_csv("wind label average hourly.csv")