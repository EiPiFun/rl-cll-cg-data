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

$python_name plot_energy.py ./cg_nve_cut_log.lammps $image_file_extension

for i in 36 81 144;do

$python_name plot.py ./all_atom/temperature_$i.xvg.txt ./coarse_grained/temperature_$i.txt '' 'Time (ns)' 'Temperature' '0.001' '1.0' '0.001' '1.0' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' temperature_$i $image_file_extension

$python_name plot.py ./all_atom/smoothed_pressure_yy_$i.xvg.txt ./coarse_grained/smoothed_pressure_yy_$i.txt '' 'Time (ns)' 'Pressure YY (GPa)' '0.001' '0.0001' '0.001' '0.0001' 'All atom' 'Coarse grained' 'dodgerblue' 'orangered' smoothed_pressure_yy_$i  $image_file_extension

done


