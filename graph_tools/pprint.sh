#pretty prints .dat file in csv to show on xyplane
#usage : sh pprint.sh <filename> <colnums+1>
#example: sh pprint.sh xyiris.dat 2,3 ----> xyiris.dat has only 2 cols: 1 and 2

python csver.py $1 | cut -d',' -f1,$2 

