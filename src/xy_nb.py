#! /usr/bin/env python
from lib import *
from reader import *
from xval import *
from math import *

def xy_nb(t,data,hypotheses,total,z,k,m,check):
    got = xy_likelyhood(t,data,total,hypotheses,z,k,m,check)
    return got

def xy_likelyhood(t,data,total,hypotheses,z,k,m,check):
    like = -0.1*10**23
    best = ''
    total += k*len(hypotheses)
    l = {}
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
            if check == True: print y,"norm value for",c
            if y == 0 or y > 1.0: y=1.0
            tmp += log(y)
        l[h] = tmp
        #if check == True: print "like:",like,"tmp:",tmp
        if tmp >= like:
            like = tmp;
            best = h
    if check == True: print "likelyhood:",l
    return best
