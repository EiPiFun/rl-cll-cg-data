#!/usr/bin/sh

python_name=python3
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi

if [ $# -gt 1 ];then
image_file_extension=$2
fi

for i in vertical;do
$python_name compare_data_distribution.py ./all_atom/"$i"_max_stress.txt ./coarse_grained/"$i"_max_stress.txt 'Max stress (MPa)' '1.0' 'All atom' 'Coarse grained' 11 6 max_stress_$i $image_file_extension
$python_name compare_data_distribution.py ./all_atom/"$i"_max_strain_energy.txt ./coarse_grained/"$i"_max_strain_energy.txt 'Max strain energy (MPa)' '1.0' 'All atom' 'Coarse grained' 12 10 max_strain_energy_$i $image_file_extension
done

for i in horizontal;do
$python_name compare_data_distribution.py ./all_atom/"$i"_max_stress.txt ./coarse_grained/"$i"_max_stress.txt 'Max stress (MPa)' '1.0' 'All atom' 'Coarse grained' 20 5 max_stress_$i $image_file_extension
$python_name compare_data_distribution.py ./all_atom/"$i"_max_strain_energy.txt ./coarse_grained/"$i"_max_strain_energy.txt 'Max strain energy (MPa)' '1.0' 'All atom' 'Coarse grained' 18 10 max_strain_energy_$i $image_file_extension
done

for i in slant;do
$python_name compare_data_distribution.py ./all_atom/"$i"_max_stress.txt ./coarse_grained/"$i"_max_stress.txt 'Max stress (MPa)' '1.0' 'All atom' 'Coarse grained' 6 10 max_stress_$i $image_file_extension
$python_name compare_data_distribution.py ./all_atom/"$i"_max_strain_energy.txt ./coarse_grained/"$i"_max_strain_energy.txt 'Max strain energy (MPa)' '1.0' 'All atom' 'Coarse grained' 11 10 max_strain_energy_$i $image_file_extension
done


