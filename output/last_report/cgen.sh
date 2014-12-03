python mmm.py dats/'acc_'$1'.dat' > mydata.dat
cat mydata.dat
gnuplot<<EOF
set terminal postscript eps color "Helvetica" 9
set boxwidth 0.2
set size 0.5,0.5
set datafile separator " "
set xrange[0:3]
set yrange[-1:25]
set title "accuracy"
set output "mydata.eps"
plot 'mydata.dat' using 1:3:2:6:5:xticlabels(8) with candlesticks notitle whiskerbars, '' using 1:4:4:4:4 with candlesticks lt -1 lw 2 notitle
EOF
epstopdf "mydata.eps"
cp mydata.pdf pdfs/'acc_'$1'.pdf'
convert -density 288 -background white -alpha off mydata.pdf -resize 40% jpegs/'acc_'$1'.jpeg'
rm mydata.dat
rm mydata.eps
rm mydata.pdf


