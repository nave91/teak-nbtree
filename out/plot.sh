gnuplot<<EOF
set terminal postscript eps color "Helvetica" 15
set size 0.5,0.5
set xtics (0,0.2,0.4,0.6,0.8,1.0)
set output "mydata.eps"
set title "weather"
set datafile separator ","
plot 'mydata.dat'  using 2:3 
EOF
epstopdf "mydata.eps"
