#! /usr/env python
from xy_lib import *
class row:
    def __init__(i,row):
        i.row = row
        i.x = 0
        i.y = 0

class xy:
    def __init__(i,t,tx,ty):
        i.xs=0
        i.ys=0
        i.kept=[]
        i.trow = row(t)
        i.trow.x = tx
        i.trow.y = ty
        

    def keep(i,xyz):
        i.kept+=[xyz]
        i.xs+=xyz.x
        i.ys+=xyz.y
    
    def addtrow(i,test):
        i.trow = test

    def tiles(i,more,mini,oldn,oldd,spy=False,lvl=0):
        n = len(i.kept)
        repeat = True
        if int(n) == int(oldn) or int(n) == 0:
            repeat = False
            if int(n) != 0:
                yield i.kept
        oldn = n
        newd = 0
        if n != 0:
            xmu = i.xs*1.0/n
            ymu = i.ys*1.0/n
            add = []
            add.append(xmu)
            add.append(ymu)
            newd = eucldist(add,i)
            #print oldd,newd
            if spy:
                print '|--'*lvl+str(n),"d:",newd,"xmuymu:",xmu,ymu
#            if oldd < newd: 
#                repeat = False
#                yield i.kept
            oldd = newd
        if repeat == True:
            if n>mini:
                if n<more:
                    yield i.kept
                else:
                    hh = i.__class__(i.trow.row,i.trow.x,i.trow.y)
                    hl = i.__class__(i.trow.row,i.trow.x,i.trow.y)
                    lh = i.__class__(i.trow.row,i.trow.x,i.trow.y)
                    ll = i.__class__(i.trow.row,i.trow.x,i.trow.y)
                    for xyz in i.kept:
                        if xyz.x < xmu:
                            if xyz.y < ymu:
                                what = ll
                            else:
                                what = lh
                        else:
                            if xyz.y < ymu:
                                what = hl
                            else:
                                what = hh
                        what.keep(xyz)
                    for xy in [ll,lh,hl,hh]:
                        for one in xy.tiles(more,mini,oldn,oldd,spy,lvl+1):
                            yield one
    
