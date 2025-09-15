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

$python_name plot.py ./all_atom/rdf.xvg.txt ./coarse_grained/rdf.xvg.txt '' ' (nm)' 'RDF' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rdf $image_file_extension

$python_name plot.py ./all_atom/rg.xvg.txt ./coarse_grained/rg.xvg.txt '' 'Time (ps)' 'Rg (nm)' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rg  $image_file_extension

$python_name plot.py ./all_atom/rmsd.xvg.txt ./coarse_grained/rmsd.xvg.txt '' 'Time (ps)' 'RMSD (nm)' '1.0' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' rmsd  $image_file_extension


