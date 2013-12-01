from reader import *
from dist import *
from sys import *
from table import *
from xy import *

def leafprint(leaves):
    for key,leaf in leaves.items():
        print ""
        print key
        for i in leaf:
            print "\t\t",i.row

def leaftab(leaves):
    ltab = {} #ltab is leaf tables with each leaf in ltab[0]..ltab[n]
    for key,leaf in leaves.items():
        ltab[key] = [0,0] #ltab[key][0] = xmu's [1]=ymu's
        ilen = 0 #number of rows
        for i in leaf:
            ltab[key][0]+=i.x
            ltab[key][1]+=i.y
            ilen+=1
        ltab[key][0] = ltab[key][0]/ilen
        ltab[key][1] = ltab[key][1]/ilen
    return ltab

def xy_proj(z,data):
    xyobj = xy()
    d  = anyi(data[z])
    print len(data[z]),"lennnn"
    if d == len(data[z]):
        d-=1
    x = [0]*len(data[z])
    y = [0]*len(data[z])
    east = furthest(d,data,z)
    west = furthest(data[z].index(east),data,z)
    inde = data[z].index(east)
    indw = data[z].index(west)
    c = dist(data[z][inde],data[z][indw],data,z,indep,nump)
    xyobj = xy_proj0(inde,indw,c,data,z,x,y,count)
    leaves = {}
    for n,leaf in enumerate(xyobj.tiles(20,4)):
        #print leaf
        leaves[n] = leaf
    #leafprint(leaves)
    ltab = leaftab(leaves)
    for key,leaf in ltab.items():
        print leaf[0],leaf[1]
            
    

def xy_proj0(east,west,c,data,z,x,y,count):
    print "+"
    bigger = 1.05
    some = 0.000001
    xyobj = xy()
    for d in data[z]:
        ind = data[z].index(d)
        a = dist(data[z][ind],data[z][east],data,z,indep,nump)
        b = dist(data[z][ind],data[z][west],data,z,indep,nump)
        x[ind] = (a**2 + c**2 - b**2) / (2*c + some)
        y[ind] = (a**2 - x[ind]**2)**0.5
        r = row(d)
        r.x = x[ind]
        r.y = y[ind]
        #print r.row
        xyobj.keep(r)
    return xyobj
        

    
        
