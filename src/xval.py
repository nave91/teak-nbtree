#! /usr/bin/env python
from lib import *
from reader import *
from table import *
from zeror import *
from nb import *

def xvals(data,x,b,f,z,k,m):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            xval(b1*s, (b1+1)*s, data, rows, f, z, k, m)
        x=x-1

def  xval(start, stop, data, rows, f, z, k, m):
    rmax = len(rows)
    test = []
    hypotheses = {}
    temp = ""
    #newddict(data,z)
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
    nb(test,data,hypotheses,z,k,m)


def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
