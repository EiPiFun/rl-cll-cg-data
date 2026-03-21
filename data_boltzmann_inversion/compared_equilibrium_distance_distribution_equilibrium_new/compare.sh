#!/usr/bin/sh

python_name=python3
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi

if [ $# -gt 1 ];then
image_file_extension=$2
fi

rm ./*.$image_file_extension

i=11;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 20 11 $i $image_file_extension
i=12;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 20 12 $i $image_file_extension
i=13;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 20 14 $i $image_file_extension
i=22;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 20 12 $i $image_file_extension
i=23;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 20  9 $i $image_file_extension
i=33;$python_name compare_data_distribution.py ./all_atom/$i.txt ./coarse_grained/$i.txt 'Equilibrium distance (nm)' '1.0' 'All atom' 'Coarse grained' 30 15 $i $image_file_extension

