from reader import *
from dist import *
from sys import *
from table import *
from xy import *
from xy_lib import *
from xy_globfile import *
def xy_proj(z,data,t,tz,check):
    #xyobj = xy()
    d  = anyi(data[z])
    if d == len(data[z]):
        d-=1
    x = [0]*len(data[z])
    y = [0]*len(data[z])
    east = furthest(d,data,z)
    west = furthest(data[z].index(east),data,z)
    inde = data[z].index(east)
    indw = data[z].index(west)
    c = dist(data[z][inde],data[z][indw],data,z,indep,nump)
    xyobj = xy_proj0(t,inde,indw,c,data,z,x,y,count,tz)
    leaves = {}
    oldd = 999999
    for n,leaf in enumerate(xyobj.tiles(20,4,0,oldd)):
        leaves[n] = leaf
    #if check == True: leafprint(leaves)
    if check == True: print "nearest d",xy_d#,"nearest node",xyobj.nearest
    if check == True: print "test row:",xyobj.trow.x,xyobj.trow.y
    ltab = leaftab(leaves)
    if check == True: printltab(ltab)
    close = nearleaf(ltab,xyobj)
    if check  == True: checkie(leaves,ltab,close,data,tz,t)
    
    return out_reduced(leaves,close)

def xy_proj0(t,east,west,c,data,z,x,y,count,tz):
    #print "+"
    bigger = 1.05
    some = 0.000001
    #xyobj = xy()
    #calculating test row's x and y coordinates
    trow = row(data[tz][t])
    #xyobj.addtrow(trow)
    ta = dist(data[tz][t],data[z][east],data,z,indep,nump)
    tb = dist(data[tz][t],data[z][west],data,z,indep,nump)
    #xyobj.trow.x = (ta**2 + c**2 - tb**2) / (2*c + some)
    #xyobj.trow.y = (ta**2 - xyobj.trow.x**2)**0.5
    tx = (ta**2 + c**2 - tb**2) / (2*c + some)
    ty = (ta**2 - tx**2)**0.5
    xyobj = xy(t,tx,ty)
    #print xyobj.trow.x,xyobj.trow.y
    for d in data[z]:
        ind = data[z].index(d)
        a = dist(data[z][ind],data[z][east],data,z,indep,nump)
        b = dist(data[z][ind],data[z][west],data,z,indep,nump)
        x[ind] = (a**2 + c**2 - b**2) / (2*c + some)
        y[ind] = (a**2 - x[ind]**2)**0.5
        r = row(d)
        r.x = x[ind]
        r.y = y[ind]
        xyobj.keep(r)
    return xyobj
        

    
        
