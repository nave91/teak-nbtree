#! /usr/env python

class xy:
    def __init__(i):
        x = 0
        y = 0
        row = []
        i.xs=0
        i.ys=0
        i.kept=[]
    def keep(xyz):
        i.kept+=[xyz]
        i.xs+=xyz.x
        i.ys+=xyz.y
    def tiles(i,more,min,spy=False,lvl=0):
        n = len(kept)
        if n>min:
            if n<max:
                yield i.kept
            else:
                if spy:
                    print '|--'*lvl+str(n)
                xmu = i.xs*1.0/n
                ymu = i.ys*1.0/n
                hh,hl,lh,ll=xy(),xy(),xy(),xy()
                for xyz in i.kept:
                    if xyz.x < xmu:
                        what = ll if xyz.x < ymu else lh
                    else:
                        what = hl if xyz.x < ymu else hh
                    what.keep(xyz)
                for xy in [ll,lh,hl,hh]:
                    for one in xy.tiles(more,min,spy,lvl+1):
                        yield one
