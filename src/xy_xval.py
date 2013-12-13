#! /usr/bin/env python
from lib import *
from reader import *
from table import *
from zeror import *
from xy_nb import *
from xy_proj import *
from abcd import *
import sys

def xy_xvals(data,x,b,f,z,k,m,check=False):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    acc = []
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            abcd = Abcd()
            #include this in acc.append() to get accuracy
            xy_xval(b1*s,(b1+1)*s,data,rows,f,z,k,m,check,abcd) 
            #acc.append(xy_xval(b1*s,(b1+1)*s,data,rows,f,z,k,m,check,abcd)) 
            abcd.header()
            abcd.report()
        x=x-1
        
    #for i in sorted(acc): #for accuracy
    #    print i,

def xy_xval(start,stop,data,rows,f,z,k,m,check,abcd):
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
#        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        ind = data[z].index(ts)#index of test row in data[z]
        l = "__aft"+str(test.index(ts))
        dafter = xy_proj(bef,data,ind,z,check)
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
        got = xy_nb(ts,data,hypotheses,total,l,k,m,check)
        #check what we are expecting and getting
        if check == True: print "want:",want,"got:",got 
        if want == got: acc+=1.0
        if check == True: sys.exit() #exit after a round
        abcd.keep(want,got)
    #return round(100*acc/len(test),2) #To get accuracy


def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
