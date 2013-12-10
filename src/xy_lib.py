#library for xy_*.py
from table import *
from reader import *

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
    print "leaf tables mean x and y"
    for key,leaf in ltab.items():
        print key,leaf[0],leaf[1]

def eucldist(leaf,xyobj):
    d1 = d2 = 0.0
    #print leaf,"leaffffff"
    #print xyobj.trow.x,xyobj.trow.y,"x,y"
    d1 = (xyobj.trow.x - leaf[0])**2
    d2 = (xyobj.trow.y - leaf[1])**2
    d = (d1+d2)**0.5
    #print d,"ddd"
    return d

def nearleaf(ltab,xyobj):
    #print "distances from test row to leaves"
    small = 10**23
    smallind = 0
    for key,leaf in ltab.items():
        tmp = eucldist(leaf,xyobj)
        #print key,tmp
        if tmp < small:
            small = tmp
            smallind = key
    return smallind
        
def out_reduced(leaves,close):
    tmp = []
    for i in leaves[close]:
        tmp.append(i.row)
    return tmp


def hypbuild(data,z):
    hypotheses = {}
    for d in data[z]:
        temp = klass1(d, z)
        try:
            hypotheses[temp] += 1
            if hypotheses[temp] == 1:
                makeTable(colname[z],temp)
            addRow(d,temp)
        except KeyError:
            hypotheses[temp] = 1
            if hypotheses[temp] == 1:
                makeTable(colname[z],temp)
            addRow(d,temp)
    return hypotheses
   
def checkie(leaves,ltab,close,data,tz,t):
    #printltab(ltab)
    #leafprint(leaves)
    print ">>close",close
    print "+test:",data[tz][t]
    print "closest leaf:",close,":",out_reduced(leaves,close),"len:",len(leaves[close])

    
