#!/usr/env python

from sys import *

def line(file):
    l = file.readline()
    if l != '':
        l = l.replace('\n','')
        l = l.split(' ')
        l = [i for i in l if i != '' ]
    return l

file = open(argv[1],'r')
s=''
j=0
while True:
    lst = line(file)
    if not lst:
        break
    j+=1
    s+=str(j)+','
    for i in lst:
        s+=i+','
    s+='\n'
print s    
