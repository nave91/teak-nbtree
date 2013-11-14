from reader import *
from  xval import *
from lib import *

def zeror(test,data,hypotheses,z):
    hmost = -10**23
    acc = 0
    got = ""
    for h in hypotheses:
        these = len(data[h])
        if these > hmost:
            hmost = these
            got = h
    #print "#got: ",got
    where = klassAt(z)
    for t in test:
        want = t[where]
        if want == got:
            acc+=1.0
    print '%0.2f' % round(100*acc/len(test),2),
