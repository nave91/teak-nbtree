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

    def keep(i,xyz):
        i.kept+=[xyz]
        i.xs+=xyz.x
        i.ys+=xyz.y

    def tiles(i,more,mini,spy=False,lvl=0):
        n = len(i.kept)
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
                        what = ll if xyz.x < ymu else lh
                    else:
                        what = hl if xyz.x < ymu else hh
                    what.keep(xyz)
                for xy in [ll,lh,hl,hh]:
                    for one in xy.tiles(more,mini,spy,lvl+1):
                        yield one
