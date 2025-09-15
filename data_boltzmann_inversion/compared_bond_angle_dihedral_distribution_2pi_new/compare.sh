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

i=bond_cl1-cl1.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Bond length (nm)' '1.0' 'All atom' 'Coarse grained' 18 20 $i $image_file_extension
i=bond_cl1-cl2.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Bond length (nm)' '1.0' 'All atom' 'Coarse grained' 20 20 $i $image_file_extension
i=bond_cl1-cl3.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Bond length (nm)' '1.0' 'All atom' 'Coarse grained' 18 20 $i $image_file_extension

i=angle_cl1-cl1-cl1.txt  ;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained' 15 20 $i $image_file_extension
i=angle_cl2-cl1-cl1_1.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained' 15 20 $i $image_file_extension
i=angle_cl2-cl1-cl1_2.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained' 13 20 $i $image_file_extension
i=angle_cl2-cl1-cl3.txt  ;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained' 15 20 $i $image_file_extension
i=angle_cl3-cl1-cl1_1.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained'  8 20 $i $image_file_extension
i=angle_cl3-cl1-cl1_2.txt;$python_name compare_data_distribution.py ./all_atom/$i ./coarse_grained/$i 'Angle size' '1.0' 'All atom' 'Coarse grained' 10 20 $i $image_file_extension

i=dihedral_cl1-cl1-cl1-cl1.txt;$python_name compare_data_distribution_cut.py ./all_atom/$i ./coarse_grained/$i 'Dihedral size' '1.0' 'All atom' 'Coarse grained' 11 20 $i $image_file_extension
i=dihedral_cl2-cl1-cl1-cl3.txt;$python_name compare_data_distribution_cut.py ./all_atom/$i ./coarse_grained/$i 'Dihedral size' '1.0' 'All atom' 'Coarse grained' 14 20 $i $image_file_extension
i=dihedral_cl3-cl1-cl1-cl2.txt;$python_name compare_data_distribution_cut.py ./all_atom/$i ./coarse_grained/$i 'Dihedral size' '1.0' 'All atom' 'Coarse grained' 16 20 $i $image_file_extension


