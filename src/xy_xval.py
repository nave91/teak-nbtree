#! /usr/bin/env python
from lib import *
from reader import *
from table import *
from zeror import *
from xy_nb import *
from xy_proj import *
import sys
def xy_xvals(data,x,b,f,z,k,m):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    acc = []
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            acc.append(xy_xval(b1*s,(b1+1)*s,data,rows,f,z,k,m))
        x=x-1
    for i in sorted(acc):
        print i,

def xy_xval(start,stop,data,rows,f,z,k,m,check=False):
    rmax = len(rows)
    test = []
    hypotheses = {}
    temp = ""
    acc = 0.0
    for r in range(start,stop):
        d = rows[r]
        test.append(d)
    bef = "__bef"
    makeTable(colname[z],bef)
    for r in range(0,rmax):
        d = rows[r]
        addRow(d,bef)
    for ts in test:
        ind = data[z].index(ts)#index of test row in data[z]
        l = "__aft"+str(test.index(ts))
        dafter = xy_proj(bef,data,ind,z)
        makeTable(colname[z],l)
        for r in range(0,len(dafter)):
            d = dafter[r]
            addRow(d,l)
            if check ==True: tableprint(l) #print each leaf table
        hypotheses = hypbuild(data,l)
        where = klassAt(l)
        total = 0.0
        for h in hypotheses:
            total += len(data[h])
        want = ts[where]
        got = xy_nb(ts,data,hypotheses,total,l,k,m)
        if check == True: print want,got #check what we are expecting and getting
        if want == got: acc+=1.0
        #sys.exit()
    return round(100*acc/len(test),2)
    #print '%0.2f' % round(100*acc/len(test),2),


def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
