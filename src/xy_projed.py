#gives output to project on an xy plane
#usage: python xy_projed.py "<data set name>" "both" ""

from reader import *
from sys import argv
from table import *
from xy_proj import *

def xy_projed():
    csvfile = open('../data/'+argv[1]+'.csv','r')
    readCsv(csvfile,argv[2])
    #tableprint(argv[2])
    xy_proj(argv[2],data)
    #tableprint(w)

xy_projed()
