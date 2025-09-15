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

rm ./*.$image_file_extension

for i in vertical horizontal slant;do
$python_name plot_smoothed_stress-strain_with_reference.py ./all_atom/"$i"_strain_y_stretch.xvg.txt ./all_atom/"$i"_smoothed_stress_y_stretch.xvg.txt ./"$i"_box_size-pressure_stretch y $image_file_extension
done

$python_name plot_direction_angle-strain_with_reference.py ./all_atom/slant_strain_y_stretch.xvg.txt ./all_atom/stretch_direction_angle.txt ./slant_box_size-pressure_stretch y ./cl_average_direction_angle_stretch.txt $image_file_extension


