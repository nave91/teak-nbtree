#! /usr/bin/env python
from reader import *

def dist(this,that,data,z,indep,nump):
    tot = 0.0
    for k in indep[z]:
        ind = colname[z].index(k)
        v1 = this[ind]
        v2 = that[ind]
        #print ">","v1",v1,"v2",v2
        if v1 == "?" and v2 == "?":
            tot+=1
        elif k in nump[z]:
            aLittle = 0.0000001
            mid = (hi[z][k] - lo[z][k])/2
            if v1 == "?":
                v1 = 1 if v2 < mid else 0
            else:
                v1 = (v1 - lo[z][k])/ (hi[z][k] - lo[z][k] + aLittle)
            if v2 == "?":
                v2 = 1 if v1 < mid else 0
            else:
                v2 = (v2 - lo[z][k])/ (hi[z][k] - lo[z][k] + aLittle)
            tot += (v2-v1)**2
        else:
            if v1 == "?":
                tot += 1
            elif v2 == "?":
                tot += 1
            elif v1 != v2:
                tot += 1
            else:
                tot += 0
    ret = tot**0.5 / (len(indep[z]))**0.5
    return ret

def closest(i,z,selfie,data):
    mini = 0.0001
    indi = data[z].index(i)
    for j in data[z]:
        if i == j and i != selfie:
            continue
        d = dist(data[z][i],data[z][j],data,z,indep,nump)
        if d > maxi:
            maxi = d
            out = j
    return out

def furthest(i,data,z):
    maxi = -1
    out = 0
    for j in data[z]:
        d = dist(data[z][i],j,data,z,indep,nump)
        if d > maxi:
            maxi = d
            out = j
    return out
