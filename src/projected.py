from project import *
from reader import *
from sys import argv
from table import *
def projected():
    projected1("data/automsg.csv")

def projected1(f):
    csvfile = open('../data/'+argv[1]+'.csv','r')
    readCsv(csvfile,argv[2])
    w = project(argv[2],data)
    tableprint(w)

projected()
