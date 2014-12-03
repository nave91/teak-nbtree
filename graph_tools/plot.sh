#plots on a xy plane and converts it into pdf
#usage sh plot.sh

gnuplot<<EOF
set terminal postscript eps color "Helvetica" 15
set size 1,1
#set xtics (0,0.2,0.4,0.6,0.8,1.0)
set output "mydata.eps"
set title "diabetes"
set datafile separator ","
plot 'mydata.dat'  using 2:3 
EOF
epstopdf "mydata.eps"
