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
echo "Image file extension: $image_file_extension"

for i in all layer interlayer;do

$python_name plot.py ./all_atom/rdf_$i.xvg.txt ./coarse_grained/rdf_$i.xvg.txt '' 'r (nm)' 'RDF' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rdf_$i $image_file_extension

$python_name plot.py ./all_atom/rg_$i.xvg.txt ./coarse_grained/rg_$i.xvg.txt '' 'Time (ps)' 'Rg (nm)' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rg_$i  $image_file_extension

$python_name plot.py ./all_atom/rmsd_$i.xvg.txt ./coarse_grained/rmsd_$i.xvg.txt '' 'Time (ps)' 'RMSD (nm)' '1.0' '1.0' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rmsd_$i  $image_file_extension

done

