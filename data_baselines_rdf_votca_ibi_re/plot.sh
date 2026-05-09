#!/usr/bin/bash

python_name=python3
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi

if [ $# -gt 1 ];then
image_file_extension=$2
fi

echo "Python name: $python_name"
echo "Image file extension: $image_file_extension"

for i in ibi re;do
for j in 1 2 3;do
for ((k=j;k<=3;k++));do

$python_name plot.py ./all_atom/rdf_cl"$j"_cl"$k".xvg.txt ./coarse_grained/"$i"_rdf_cl"$j"_cl"$k".xvg.txt '' 'r (nm)' 'RDF' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' "$i"_rdf_cl"$j"_cl"$k".xvg $image_file_extension

done
done
done


