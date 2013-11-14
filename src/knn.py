
#! /usr/bin/env python
from reader import *
from table import *
from dist import *
import sys
def knn(test,data,z,a,k):
    acc = 0.0
    if a == "--once":
        print "#the training data"
        tableprint1(z)
    where = klassAt(z)
    for t in test:
        want = t[where]
        got = knn1(t,data,z,a,where,k)
        if want == got:
            acc+=1.0
        if a == "--once":
            print want,got
            sys.exit()
    print '%0.2f' % round(100*acc/len(test),2),

def knn1(t,data,z,a,where,k):
    seen = {}
    #lst = [{} for i in range(0,len(data[z]))]
    lst = []
    sort = neighbors(t, data, z, lst)
    if a == "--once":
        print "#the test row"
        print rowprint(t)
        print "#the distances"
        for i in range(0,len(sort)):
            print i,round(sort[i]['x'],5),rowprint(sort[i]['d'])
    nearestk(k,data,z,where,sort,seen)
    return mostSeen(seen)

def neighbors(t,data,z,lst):
    for d in data[z]:
        ind = data[z].index(d)
        dic = {}
        dic['x'] = dist(t,d,data,z,indep[z],nump[z])
        dic['d'] = d
        lst.append(dic)
        #lst[ind]['x'] = dist(t,d,data,z,indep[z],nump[z])
        #lst[ind]['d'] = d
    """print "lsttttttttttttttttttttttt"
    for i in range(0,len(lst)):
        try:
            print lst[i]
            print lst[i]['x'];
            print i
        except KeyError:
            lst[i]['x'] = -1
            lst[i]['d'] = []
            """
    sort = sorted(lst, key=lambda lst: lst['x'])
    return sort

def nearestk(k,data,z,where,sort,seen):
    for i in range(0,k):
        that = sort[i]['d']
        ind = data[z].index(that)
        got = data[z][ind][where]
        try:
            seen[got] += 1
        except KeyError:
            seen[got] = 1

def mostSeen(seen):
    maxi = -10**23
    for x in seen:
        if seen[x] > maxi:
            maxi = seen[x]
            out = x
    return out
            
