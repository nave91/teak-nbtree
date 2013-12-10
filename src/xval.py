#! /usr/bin/env python
from lib import *
from reader import *
from table import *
from zeror import *
from nb import *

def xvals(data,x,b,f,z,k,m):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    acc = []
    abcd = Abcd()
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            abcd = Abcd()
            #include in acc.append() for acc
            #xval(b1*s,(b1+1)*s,data,rows,f,z,k,m,abcd)
            acc.append(xval(b1*s,(b1+1)*s,data,rows,f,z,k,m,abcd))
            #abcd.header()
            #abcd.report()

        x=x-1
    for i in sorted(acc):
        print i,

def xval(start,stop,data,rows,f,z,k,m,abcd):
    rmax = len(rows)
    test = []
    hypotheses = {}
    temp = ""
    for r in range(0, rmax):
        d = rows[r]
        if r >= start and r < stop:
            test.append(d)
        else:
            temp = klass1(d, z)
            try:
                hypotheses[temp] += 1
                if hypotheses[temp] == 1:
                    makeTable(colname[z],temp)
                addRow(d,temp)
            except KeyError:
                hypotheses[temp] = 1
                if hypotheses[temp] == 1:
                    makeTable(colname[z],temp)
                addRow(d,temp)
    #zeror(test, data, hypotheses, z) 
    #xvalTest1(test,data,hypotheses)
    return nb(test,data,hypotheses,z,k,m,abcd)
    #nb(test,data,hypotheses,z,k,m,abcd)

def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
