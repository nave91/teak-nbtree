Proj=$1
Title="573:"$Proj":Naveen Kumar Lekkalapudi"
echo $Title
a2ps --center-title="$Title" -o $Proj.ps ~/git/teak-nbtree/tmp/*
ps2pdf $Proj.ps
