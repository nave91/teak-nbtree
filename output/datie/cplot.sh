gnuplot<<EOF
set terminal postscript eps color "Helvetica" 9
set boxwidth 0.2
set size 0.5,0.5
set datafile separator " "
set xrange[0:3]
set yrange[60:90]
set title "accuracy"
set output "mydata.eps"
plot 'mydata.dat' using 1:3:2:6:5:xticlabels(8) with candlesticks notitle whiskerbars, '' using 1:4:4:4:4 with candlesticks lt -1 lw 2 notitle
EOF
epstopdf "mydata.eps"
