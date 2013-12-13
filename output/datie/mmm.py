

#!/usr/env python
#usage: python mmm.py dats/acc_*.dat

#Used to generate min,q1,med,q3,high of the input data which can be 
#used to generate plot graphs
from sys import *

file = open(argv[1],'r')
s=''
j=0
name = []
value = []
maxi = -10
mini = 9999
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

def medind(i):
    l = len(i)
    medi = 0.0
    if l%2 == 0: medi = l/2 
    else: medi = l/2+1
    return medi

def lo(i,nedi):
    temp1 = []
    for j in range(0,len(i)):
        if j < nedi:
            temp1.append(i[j])
    return temp1

def hi(i,nedi):
    temp1 = []
    for j in range(0,len(i)):
        if j > nedi:
            temp1.append(i[j])
    return temp1
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
    medi = len(i)/2*1.0
    low = []
    high = []
    low = lo(i,medi)
    high = hi(i,medi)
    #for j in range(0,len(i)):
    #    if j < medi:
    #        low.append(i[j])
    #    else:
    #        high.append(i[j])
    q1 = median(low)
    q3 = median(high)
    tmp.append([min(i),q1,med,q3,max(i)])

for i in tmp:
    print int(tmp.index(i))+1,
    for j in i:
        print str(j),
    print "1 "+name[tmp.index(i)]
    
