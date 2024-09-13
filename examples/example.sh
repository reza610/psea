
infile=$HOME/psea/testdata/testdata.csv
outdirname=$HOME/outpsea/
outfilename=${outdirname}testdata.csv

mkdir $outdirname

python3 ../src/psea_orginal.py -i $infile -o $outfilename

echo $outfilename
