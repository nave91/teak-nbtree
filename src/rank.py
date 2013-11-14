from lib import *
import re
from globfilerank import *

def obs(f,alli):
    now = alli
    line = f.readline()
    while(line):
        lst = line.split()
        for i in lst:
            isitnum = re.match('^([^0-9]|\.)',i)
            if isitnum:
                now = i
            else:
                v = float(i)
                inc(v,now)
                inc(v,alli)
        for i in name:
            if i != alli:
                temp = {}
                temp["="] = i
                temp["x"] = mu[i]
                order.append(temp)
        line = f.readline()

def inc(v,k):
    print v,"vvvvvvvvvvvvvvvvvvv"
    print k,"kkkkkkkkkkkkk"
    name.append(k)
    label[k] = 0
    try:
        n[k] += 1
    except KeyError:
        n[k] = 1
    alli = n[k]
    try:
        x[k][alli] = v
    except KeyError:
        x[k] = {}
        x[k][alli] = v
    try:
        sumi[k] += v
    except KeyError:
        sumi[k] = v
    try:
        delta = v - mu[k]
    except KeyError:
        mu[k] = 0
        delta = v - mu[k]
    try:
        mu[k] += delta/alli
    except KeyError:
        mu[k] = delta/alli
    try:
        m2[k] += delta*(v - mu[k])
    except KeyError:
        m2[k] = delta*(v - mu[k])
    var[k] = m2[k]/(alli - 1 + PINCH)

def rank(alli,cohen,mittas,a12):
    cohen = cohen*(var[alli])**0.5
    level = 0 
    total = n[alli]
    rdiv(0,len(order)-1,1,cohen,mittas,a12,level)
    
def rdiv(low,high,c,cohen,mittas,a12,level):
    cut = div(low,high,cohen,mittas,a12)
    if cut:
        print "in cut",cut
        level += 1
        c = rdiv(low,cut-1,c,cohen,mittas,a12,level) + 1
        c = rdiv(cut,high,c,cohen,mittas,a12,level)
    else:
        for i in range(low,high):
            print order[i]["="],"orderrrrrrrrrr",c
            label[order[i]["="]] = c
    return c

def div(low,high,cohen,mittas,a12):
    n0 = [0 for i in range(0,len(order))]
    n1 = [0 for i in range(0,len(order))]
    sum0 = [0 for i in range(0,len(order))]
    sum1 = [0 for i in range(0,len(order))]
    muAll = divInits(low,high,n0,n1,sum0,sum1)
    maxi = -1
    cut = 0
    for i in range(low,high):
        b = order[i]["="]
        n0[i] = n0[i-1] + n[b]
        sum0[i] = sum0[i-1] + sumi[b]
        left = n0[i]
        muLeft = sum0[i] / left
        right = n1[i]
        muRight = sum0[i] / right
        e = errDiff(muAll,left,muLeft,right,muRight)
        if cohen:
            if abs(muLeft - muRight) <= cohen:
                continue
        if mittas:
            if e < maxi:
                continue
        if a12:
            if bigger(low,i,high) < a12:
                continue
        maxi = e
        cut = i
    print cut,"cutttt"
    return cut

def errDiff(mu,n0,mu0,n1,mu1):
    return n0*(mu - mu0)**2 + n1*(mu - mu1)**2

def divInits(low,high,n0,n1,sum0,sum1):
    b= order[low]["="]
    n0[low]= n[b]
    sum0[low]= sumi[b]
    b= order[high]["="]
    n1[high]= n[b]
    sum1[high]= sumi[b]
    for i in range(high-1,low-1,-1):
        b = order[i]["="]
        n1[i] = n1[i+1] + n[b]
        sum1[i] = sum1[i+1] + sumi[b]
    return sum1[low+1]/n1[low+1]

def bigger(low,mid,high):
    below =  []
    above = []
    below = values(low,mid-1)
    above = values(mid,high)
    return a12statistic(below,above)

def a12statistic(below,above):
    more = 0
    same = 0
    comparisons = 1
    for j in range(0,len(above)-1):
        for i in range(0,len(below)-1):
            comparisons += 1
            more += above[j] if above[j] > below[i] else below[i]
            same += above[j] if above[j] == below[i] else below[i]
    return (more + 0.5*same)/comparisons

def values(i,j):
    out = []
    m = 0    
    for k in range(i,j):
        b = order[k]["="]
        for l,n in enumerate(x[b]):
            m += 1
            out.append(x[b][n])
    return out

def ranks(f,cohens,mittas,a12):
    print "\n----|,",f.name,"|------------------"
    obs(f,0)
    rank(0,cohens,mittas,a12)
    maxi = len(order)
    for i in range(0,maxi):
        k = order[i]["="]
        print k
        print name,"nameee"
        print mu,"muuu"
        print label,"rank"
    
        print k,name[k],":mu",mu[k],":rank",label[k]        

f = open('../data/ska.txt','r')
ranks(f,0.3,1,0.6)
f.close()
