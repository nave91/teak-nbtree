#!/usr/env python

from sys import *

file = open(argv[1],'r')
s=''
j=0
name = []
value = []
maxi = -10
mini = 9999
low = []
high = []
tmp = []

def line(file):
    l = file.readline()
    if l != '':
        l = l.replace('\n','')
        l = l.split(' ')
        l = [i for i in l if i != '' ]
    return l

def median(i):
    l = len(i)
    med = 0.0
    if l%2 == 0:
        med = (i[l/2]+i[(l/2)+1])/2
    else:
        med = i[l/2+1]
    return med

#convert into lists
while True:
    x = []
    lst = line(file)
    if not lst:
        break
    for i in lst:        
        try:
            x.append(float(i))
        except ValueError:
            name.append(str(i))

    if x != []: value.append(x)

#print out as required
for i in value:
    med = median(i)
    for j in i:
        if j < med:
            low.append(j)
        else:
            high.append(j)
    q1 = median(low)
    q3 = median(high)
    tmp.append([min(i),q1,med,q3,max(i)])

for i in tmp:
    print int(tmp.index(i))+1,
    for j in i:
        print str(j),
    print "1 "+name[tmp.index(i)]
    
