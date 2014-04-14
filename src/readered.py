from reader import *
from table import *
from sys import argv
from xval import *
from uxval import *
from xy_xval import *

csvfile = open('../data/'+argv[1]+'.csv','r')
readCsv(csvfile,argv[2]) #takes predicted value as arguement
a = argv[3]
#print "nb"
#xvals(data,5,5,'nb',argv[2],2,1)
#print ""
#print "knn"
#uxvals(data,2,2,'nb',argv[2],2,2,a)

#print "nb-tree"
xy_xvals(data,5,5,'nb',argv[2],2,1)
tableprint(argv[2])

