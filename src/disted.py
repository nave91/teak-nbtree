from reader import *
from dist import *

def disted(f):
    csvfile = open('../data/'+f+'.csv','r')
    z = "both"
    readCsv(csvfile,z)
    distedAll(csvfile,z)

def distedAll(csvfile,z):
    for i in range(0,len(data[z])):
        for j in range(0,len(data[z])):
            print dist(data[z][i],data[z][j],data,z,indep,nump)

disted("soybean")
