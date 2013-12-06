#! /usr/env python
class row:
    def __init__(i,row):
        i.row = row
        i.x = 0
        i.y = 0

class xy:
    def __init__(i):
        i.xs=0
        i.ys=0
        i.kept=[]
        i.trow = row([])

    def keep(i,xyz):
        i.kept+=[xyz]
        i.xs+=xyz.x
        i.ys+=xyz.y
    
    def addtrow(i,test):
        i.trow = test

    def tiles(i,more,mini,oldn,spy=False,lvl=0):
        n = len(i.kept)
        repeat = True
        if int(n) == int(oldn) or int(n) == 0:
            repeat = False
            if int(n) != 0: yield i.kept
        oldn = n
        if repeat == True:
            if n>mini:
                if n<more:
                    yield i.kept
                else:
                    if spy:
                        print '|--'*lvl+str(n)
                    xmu = i.xs*1.0/n
                    ymu = i.ys*1.0/n
                    hh = i.__class__()
                    hl = i.__class__()
                    lh = i.__class__()
                    ll = i.__class__()
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
                        for one in xy.tiles(more,mini,oldn,spy,lvl+1):
                            yield one
    
