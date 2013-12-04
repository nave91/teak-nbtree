from globfile import *
from lib import *
def tableprint(z): #prints table with the summary
    print rowprint(colname[z]),'%10s' % 'notes'
    print rowprint(expected(colname[z],z)), '%10s' % 'expected'
    temp = [ c for c in range(len(colname[z]))]
    for c in colname[z]:
        if c in nump[z]:
            temp[colname[z].index(c)] = str('%0.2f' % round(sd[z][c],2))
        else:
            temp[colname[z].index(c)] = str('%0.2f' % round(float(most[z][c])/float(n[z][c]),2))
    print rowprint(temp),'%10s' % 'certainity'
    for row in data[z]:
        print rowprint(row)

def tableprint1(z):
    print rowprint(colname[z])
    for row in data[z]:
        print rowprint(row)

def klass1(data, z):
    for k in klass[z]:
        return data[colname[z].index(k)]

def klassAt(z):
    for k in klass[z]:
        return colname[z].index(k)

def fromHell(row,z,more,less):
    m = 0
    out = 0
    aLittle = 0.001
    if z in more:
        for c in more[z]:
            ind = colname[z].index(c)
            if row[ind] != '?':
                m+=1
                print ind,z
                out += ((row[ind] - hi[z][c]) / (hi[z][c] - lo[z][c] + aLittle))**2
    if z in less:
        for c in less[z]:
            ind = colname[z].index(c)
            if row[ind] != '?':
                m+=1
                out += ((row[ind] - hi[z][c])/ (hi[z][c] - lo[z][c] + aLittle))**2
    return out**0.5/m**5 if m == 1 else 1
