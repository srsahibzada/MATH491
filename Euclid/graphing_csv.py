import math as math
import numpy as np
import random
from collections import defaultdict
import collections
import matplotlib.pyplot as plt
import csv

def f(t):
    return np.log(t)

directory = []
x = []
y = []
y_2 = []
dictionary = defaultdict(int)
'''def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current/n
    return new_num_string'''

with open('iterativeSubtractiveData.csv', 'rb') as csvfile:
    try:
        data = csv.reader(csvfile)
        for line in data:
            if line[0] == 'A':
                pass
            else:
                x += [line[0]]
                y += [line[3]]
                y_2 += [2.0773*math.log(float(line[0]))]
                '''directory += [[int(line[0]),int(line[1]),int(line[3])]]
                dictionary[str(line[3])] += 1'''            
    finally:
        csvfile.close()
        
'''for i in dictionary:
    x += [int(i)]
    y += [dictionary[i]]'''

print x
print y


colors = np.random.rand(15)
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(x,y)
plt.plot(x,y_2,'r--')
plt.xlabel("Length of p")
plt.ylabel("Iterarions")
plt.title("Length of Larger number vs Iterations for Fibbonachi numbers")
plt.show()