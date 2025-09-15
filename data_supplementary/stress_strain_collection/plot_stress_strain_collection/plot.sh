#!/usr/bin/sh

python_name=python3
plot_color=dodgerblue
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi
if [ $# -gt 1 ];then
plot_color=$2
fi

if [ $# -gt 2 ];then
image_file_extension=$3
fi

for i in vertical horizontal slant slant_square;do
$python_name plot_collection.py "$i"_strain_collection.txt "$i"_stress_collection.txt "" "Strain" "Stress (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension
$python_name plot_collection.py "$i"_strain_collection.txt "$i"_smoothed_stress_collection.txt "" "Strain" "Stress (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension
$python_name plot_integral_collection.py "$i"_strain_collection.txt "$i"_stress_collection.txt "" "Strain" "Stress (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension
$python_name plot_integral_collection.py "$i"_strain_collection.txt "$i"_smoothed_stress_collection.txt "" "Strain" "Stress (GPa)" "1.0" "-0.0001" $plot_color $image_file_extension
done


