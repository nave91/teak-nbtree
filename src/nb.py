#! /usr/bin/env python
from lib import *
from reader import *
from xval import *
from math import *

def nb(test,data,hypotheses,z,k,m):
    total = 0.0
    acc = 0.0
    for h in hypotheses:
        total += len(data[h])
    where = klassAt(z)
    for t in test:
        want = t[where]
        got = likelyhood(t,data,total,hypotheses,l,z,k,m)
        if want == got:
            acc+=1.0
    print '%0.2f' % round(100*acc/len(test),2),

def likelyhood(t,data,total,hypotheses,l,z,k,m):
    like = -0.1*10**23
    best = ''
    total += k*len(hypotheses)
    for h in hypotheses:
        nh = len(data[h])*0.1
        prior = (nh+k) / total
        tmp = log(prior)
        for c in term[h]:
            try:
                ind = colname[h].index(c)
                x = t[ind]
                if x == '?':
                    continue
                y = count[h][c][x]
                tmp += log((y + m*prior)/(nh+m))
            except KeyError:
                continue
        for c in num[h]:
            ind = colname[h].index(c)
            x = t[ind]
            if x == '?':
                continue
            y = norm(x, mu[h][c], sd[h][c])
            tmp += log(y)
        l[h] = tmp
        if tmp >= like:
            like = tmp;
            best = h
    return best
