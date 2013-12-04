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

    def tiles(i,more,mini,spy=False,lvl=0):
        n = len(i.kept)
        scount = 0
        if n>mini:
            if n<more:
#                for j in i.kept:
#                    print j.row
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
#                same = i.__class__()
#                print xmu,ymu
                for xyz in i.kept:
#                    print scount
#                    if xyz.x != 0 and xyz.y != 0:
#                        if int(xmu/xyz.x+ymu/xyz.y) == int(2.0):                            
#                            print "same"
#                            scount+=1
#                    if scount == 16:
#                        yield i.kept
#                        scount = 0

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
                    for one in xy.tiles(more,mini,spy,lvl+1):
                        yield one
