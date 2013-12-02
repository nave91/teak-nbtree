#library for xy_*.py

def leafprint(leaves):
    for key,leaf in leaves.items():
        print ""
        print key
        for i in leaf:
            stri = ''
            for j in i.row:
                stri +=str(j)+","
            print "\t\t"+stri

def leaftab(leaves):
    ltab = {} #ltab is summary of leaf tables with each leaf in ltab[0]..ltab[n]
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

def printltab(ltab):
    for key,leaf in ltab.items():
        print key,leaf[0],leaf[1]

def eucldist(leaf,xyobj):
    d1 = d2 = 0.0
    d1 = (xyobj.trow.x - leaf[0])**2
    d2 = (xyobj.trow.y - leaf[1])**2
    return (d1+d2)**0.5

def nearleaf(ltab,xyobj):
    small = 10**23
    smallind = 0
    for key,leaf in ltab.items():
        tmp = eucldist(leaf,xyobj)
        print key,tmp
        if tmp < small:
            small = tmp
            smallind = key
    return smallind
        


