#!/bin/usr/env python
from lib import *
from random import random
def ptile(lst,chops,width,form,low,high):
    who = {}
    wheres0 = {}
    low = 0 if low == "" else low 
    high = 100 if hi == "" else high
    form = "%3.0f" if form == ""  else form
    width = "" if width == "" else width
    bar = "|"
    out = [ " " for i in range(0,width)]
    n  = len(lst)
    sorte = sorted(lst)
    for p in chops:
        who[p] = sorte[int(float(p)*n)]
        wheres0[p] = {}
        where = int(width*(who[p] - low)/(high - low))
        wheres0[p]["x"] = where
        wheres0[p]["*"] = chops[p]
    wheres = []
    for p in wheres0:
        wheres.append(p)
    wheres = sorted(wheres)        
    w = len(wheres)
    for i in range(0,w):
        start = wheres0[wheres[i]]["x"]
        stop = width if i+1 == w else wheres0[wheres[i+1]]["x"]
        for j in range(start,stop):
            out[j] = wheres0[wheres[i]]["*"]
    out[int(width/2)] = bar
    median = sorte[int(0.5*n)]
    spread = sorte[int(0.75*n)] - sorte[int(0.25*n)]
    maxi = sorte[n-1]
    where = int(width*(median - low)/(high - low))
    out[where-1] = "*"
    sorted(who)
    return ">,"+str(l2s(out,"",None))+"<,"+str(l2sd(who,",",form))+",|"+str(round(median,3))+","+str(round(spread,3))+","+str(round(maxi,3))
    
lst = [random()**2 for i in range(0,1000)]
lst1 = [random()**0.5 for i in range(0,1000)]
chops = pairs("0.1,-,0.3, ,0.5, ,0.7,-,0.9, ".split(","))
print "square"+ptile(lst,chops,40,"%3.2f",0,1)
print "squareroot"+ptile(lst1,chops,40,"%3.2f",0,1)
