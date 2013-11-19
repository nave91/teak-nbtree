from reader import *
from table import *
from sys import argv
from xval import *
from uxval import *

csvfile = open('../data/'+argv[1]+'.csv','r')
readCsv(csvfile,argv[2]) #takes predicted value as arguement
a = argv[3]
print "nb"
xvals(data,2,2,'knn',argv[2],2,2)
print colname,"colnameee"
print nump,"moreee"
print ""
print "knn"
uxvals(data,2,2,'nb',argv[2],2,2,a)
                                 
#tableprint(argv[1])

