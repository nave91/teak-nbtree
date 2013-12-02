import re
from globfile import *
from random import *
from math import *
PI = 3.1415926535
EE = 2.7182818284 

def line(csvfile): #returns formatted line from the csvfile 
    l = csvfile.readline()
    endcommare = re.compile('.*,$')
    if l != '':
        l = l.split('#')[0]
        l = l.replace('\t','')
        l = l.replace('\n','')
        l = l.replace(' ','')
        endcomma = endcommare.match(l)
        if endcomma:
            return l+line(csvfile)
        else:
            return l
    else:
        return -1

def rowprint(row): #returns neat rows
    columns = [ "%15s" % cell for cell in row]
    columns.append("%4s" % '#')
    return ' '.join(columns)
   
def expected(row,z): #returns expected outcome
    out = [c for c in colname[z]]
    for c in row:
        if c in wordp[z]:
            out[colname[z].index(c)] = str(mode[z][c])
        else:
            out[colname[z].index(c)] = str('%0.2f' % round(mu[z][c],2))
    return out

def indexes(lst):
    out = []*len(lst)
    for i in lst:
        out[i] = i
    return out

def newdlist(name, key):
    name[key] = [] 

def newddict(name,key):
    name[key] = {}

def newddictdict(name,key,c):
    name[key][c] = {}

def indexes(data,z):
    return data[z]

def shuffled(rows):
    shuffle(rows)

def norm(x,m,s):
    s += 0.0001
    a = 1/sqrt(2*pi*(s**2))
    b = (x-m)**2/(2*s**2)
    return a*e**(-1*b)

def numberp(x):
    return isinstance(x,int)#0 if x == "" else 1 if x == (0+int(x)) else 0

def l2s(l,sep,form):
    form = form if form != "" else "%5.3f"
    s = ""
    n = len(l)
    for i in range(0,n):
        one = l[i]
        if numberp(one):
            one = format(one,form)
        s = s+sep+str(one)
    return s

def l2sd(d,sep,form):
    form = form if form != "" else "%5.3f"
    s = ""
    for i in d:
        one = d[i]
        #if numberp(one):
        #    one = format(str(one),form)
        s = s+sep+str(round(one,3))
    return s

def pairs(lst):
    tmp = {}
    i = 0
    while(i < len(lst)):
        tmp[lst[i]] = lst[i+1]
        i += 2
    return tmp

def anyi(lst):
    tmp = random()
    return int(tmp*len(lst)) + 1
