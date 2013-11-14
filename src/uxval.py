#! /bin/python
from lib import *
from reader import *
from table import *
from zeror import *
from nb import *
from knn import *

def uxvals(data,x,b,f,z,m,k,a):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            uxval(b1*s,(b1+1)*s,data,rows,f,z,m,k,a)
        x=x-1

def uxval(start,stop,data,rows,f,z,m,k,a):
    rmax = len(rows)
    test = []
    temp = ""
    makeTable(colname[z],"train")
    for r in range(0, rmax):
        d = rows[r]
        if r >= start and r < stop:
            test.append(d)
        else:
            addRow(d,"train")
    #zeror(test, data, hypotheses, z) 
    #xvalTest1(test,data,hypotheses)
    #nb(test,data,hypotheses,z,k,m)
    knn(test,data,"train",a,k)

def uxvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
