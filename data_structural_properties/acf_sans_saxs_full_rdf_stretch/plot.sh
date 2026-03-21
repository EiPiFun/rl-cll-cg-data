#!/usr/bin/sh

python_name=python3
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi

if [ $# -gt 1 ];then
image_file_extension=$2
fi

echo "Python name: $python_name"

for i in 1 2 3;do

$python_name plot.py ./all_atom/acf_cl$i.txt ./coarse_grained/acf_cl$i.txt '' 'Time (ps)' 'C(t)' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' acf_cl$i  $image_file_extension
$python_name plot.py ./all_atom/sans_cl$i.xvg.txt ./coarse_grained/sans_cl$i.xvg.txt '' 'q (1/nm)' 'I(q)' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' sans_cl$i $image_file_extension
$python_name plot.py ./all_atom/saxs_cl$i.xvg.txt ./coarse_grained/saxs_cl$i.xvg.txt '' 'q (1/nm)' 'S(q)' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' saxs_cl$i $image_file_extension

for ((j=i;j<=3;j++));do

$python_name plot.py ./all_atom/rdf_cl"$i"_cl"$j".xvg.txt ./coarse_grained/rdf_cl"$i"_cl"$j".xvg.txt '' 'r (nm)' 'RDF' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rdf_cl"$i"_cl"$j" $image_file_extension

done

done

