#! /usr/bin/env python
from lib import *
from reader import *
from table import *
from zeror import *
from xy_nb import *

def xy_xvals(data,x,b,f,z,k,m):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            xy_xval(b1*s,(b1+1)*s,data,rows,f,z,k,m)
        x=x-1

def xy_xval(start,stop,data,rows,f,z,k,m):
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
    where = klassAt(z)
    total = 0.0
    acc = 0.0
    for h in hypotheses:
        total += len(data[h])
    for t in test:
        want = t[where]
        got = xy_nb(t,data,hypotheses,total,z,k,m)
        if want == got: acc+=1.0
    print '%0.2f' % round(100*acc/len(test),2),


def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
