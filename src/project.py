from reader import *
from dist import *
from sys import *
from table import *
def project(z,data):
    d  = anyi(data[z])
    if d == len(data[z]):
        d-=1
    x = [0]*len(data[z])
    y = [0]*len(data[z])
    east = furthest(d,data,z)
    west = furthest(data[z].index(east),data,z)
    inde = data[z].index(east)
    indw = data[z].index(west)
    project0(inde,indw,data,z,x,y,count)
    return widen(z,x,y,more,less)

def project0(east,west,data,z,x,y,count):
    print "+"
    bigger = 1.05
    some = 0.000001
    c = dist(data[z][east],data[z][west],data,z,indep,nump)
    for d in data[z]:
        ind = data[z].index(d)
        a = dist(data[z][ind],data[z][east],data,z,indep,nump)
        b = dist(data[z][ind],data[z][west],data,z,indep,nump)
        if b > c*bigger:
            return project0(east,ind,data,z,x,y,count)
        if a > c*bigger:
            return project0(ind,west,data,z,x,y,count)
        #print "."
        x[ind] = (a**2 + c**2 - b**2) / (2*c + some)
        y[ind] = (a**2 - x[ind]**2)**0.5

def widen(z,x,y,more,less):
    adds = []
    adds.extend(colname[z])
    adds.extend(["$_XX"])
    adds.extend(["$_yy"])
    adds.extend(["_ZZ"])
    w = "__"+z
    makeTable(adds,w)
    for d in data[z]:
        ind = data[z].index(d)
        hell = fromHell(data[z][ind],z,more,less)
        wider = data[z][ind]
        wider.extend([x[ind]])
        wider.extend([y[ind]])
        wider.extend([0])
        addRow(wider,w)
    return w

    
        
