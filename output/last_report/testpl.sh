cp dats/'prec_'$1'.dat' mydata.dat
gnuplot<<EOF
set terminal postscript color "Helvetica" 15
set size 1,1
set xrange[0:110]
set yrange[0:110]
set xlabel "recall"
set ylabel "precision"
set output "mydata.eps"
set palette model RGB defined (0 "red",1 "blue", 2 "green")
plot 'mydata.dat' using 2:3:1 notitle with points pt 2 palette
EOF
epstopdf "mydata.eps"
convert -density 288 -background white -alpha off mydata.pdf -resize 40% jpegs/'prec_'$1'.jpeg'
rm mydata.dat
rm mydata.eps
rm mydata.pdf